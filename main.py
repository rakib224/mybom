import asyncio
import json
import os
import re
import signal
import sys
import traceback
import uuid
from datetime import datetime

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    ContextTypes, MessageHandler, filters,
)

# ==================== কনফিগ ====================
USER_BOT_TOKEN  = "8081639401:AAGqFFHtyj9ph4nM7IuvqMAQRc6hpFcZ3hI"
ADMIN_BOT_TOKEN = "8550680427:AAEubfF_biNGHnxs_EGDKDaYx6K9EOFaw6w"
ADMIN_USER_ID   = 5610589273

POINTS_FILE  = "points.json"
HISTORY_FILE = "history.json"
USERS_FILE   = "users.json"
LOCK_FILE    = "bot.lock"

POINT_COST = 1

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
WORKER_PY = os.path.join(BASE_DIR, "worker.py")

_user_pending  = {}
_admin_pending = {}
_running_tasks = {}   # uid -> {"task_id": str, "stop": Event, "proc": holder}

app_user  = None
app_admin = None

def log(*a): print("[LOG]", *a, flush=True)
def dbg(*a): print("🔍 [DEBUG]", *a, flush=True)

ANSI_RE = re.compile(r"\x1b\[[0-9;]*[a-zA-Z]")
def strip_ansi(s: str) -> str:
    return ANSI_RE.sub("", s)

# ==================== Lock ====================
def check_and_create_lock():
    if os.path.exists(LOCK_FILE):
        try:
            with open(LOCK_FILE) as f:
                old_pid = int(f.read().strip())
            try:
                os.kill(old_pid, 0)
            except OSError:
                log(f"পুরনো lock (PID {old_pid}) মৃত — সরাচ্ছি")
                os.remove(LOCK_FILE)
            else:
                print(f"❌ ইতিমধ্যে bot চলছে (PID {old_pid})।")
                print(f"   বন্ধ: kill -9 {old_pid}   অথবা   pkill -9 python")
                sys.exit(1)
        except Exception:
            try: os.remove(LOCK_FILE)
            except: pass
    with open(LOCK_FILE, "w") as f:
        f.write(str(os.getpid()))
    log(f"Lock তৈরি (PID {os.getpid()})")

def remove_lock():
    try:
        if os.path.exists(LOCK_FILE): os.remove(LOCK_FILE)
    except: pass

# ==================== স্টোরেজ ====================
def load_json(p, d):
    try:
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        log(f"load {p}: {e}")
    return d

def save_json(p, d):
    try:
        with open(p, "w", encoding="utf-8") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
    except Exception as e:
        log(f"save {p}: {e}")

def save_user(user):
    users = load_json(USERS_FILE, {})
    users[str(user.id)] = {
        "username":  (user.username or "").lower(),
        "first_name": user.first_name or "",
    }
    save_json(USERS_FILE, users)

def find_uid_by_username(username_input):
    """@user বা user → user_id বা None"""
    uname = username_input.strip().lstrip("@").lower()
    if not uname: return None
    users = load_json(USERS_FILE, {})
    for uid, info in users.items():
        if info.get("username", "").lower() == uname:
            return uid
    return None

def resolve_target(identifier):
    """
    identifier → user_id.
    digits হলে সরাসরি user_id, নাহলে username।
    """
    ident = identifier.strip().lstrip("@")
    if ident.isdigit():
        # ID — points/users-এ আছে কিনা চেক
        pts = load_json(POINTS_FILE, {})
        if ident in pts:
            return ident
        # থাকলেও দিতে পারি
        return ident
    return find_uid_by_username(ident)

def add_history(uid, phone, output, status, duration_s):
    h = load_json(HISTORY_FILE, {})
    h.setdefault(uid, []).append({
        "time":    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "phone":   phone,
        "status":  status,
        "seconds": duration_s,
        "output":  output[:800],
    })
    save_json(HISTORY_FILE, h)

# ==================== Safe Edit ====================
async def safe_edit(q, text, reply_markup=None, parse_mode="Markdown"):
    try:
        await q.edit_message_text(text, reply_markup=reply_markup, parse_mode=parse_mode)
    except Exception as e:
        if "not modified" in str(e).lower(): return
        log(f"edit FAIL: {e}")
        try:
            await q.message.reply_text(text, reply_markup=reply_markup, parse_mode=parse_mode)
        except Exception as e2:
            log(f"fallback FAIL: {e2}")

# ==================== কীবোর্ড ====================
def user_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 কাজ শুরু করুন", callback_data="u_run")],
        [InlineKeyboardButton("💰 ব্যালেন্স",     callback_data="u_bal"),
         InlineKeyboardButton("📜 হিস্টোরি",      callback_data="u_hist")],
        [InlineKeyboardButton("📞 অ্যাডমিনের সাথে যোগাযোগ", callback_data="u_contact")],
    ])

def user_back():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ মেনু", callback_data="u_home")]
    ])

def stop_button(uid, task_id):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🛑 স্টপ", callback_data=f"u_stop:{uid}:{task_id}")]
    ])

def admin_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ পয়েন্ট দিন",   callback_data="a_add"),
         InlineKeyboardButton("➖ পয়েন্ট কমান", callback_data="a_remove")],
        [InlineKeyboardButton("👥 ইউজার তালিকা", callback_data="a_users"),
         InlineKeyboardButton("📊 হিস্টোরি",     callback_data="a_history")],
    ])

def admin_back():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ মেনু", callback_data="a_home")]
    ])

# ============================================================
# ============ worker SILENT রান (শুধু Termux-এ লগ) ==========
# ============================================================
async def _kill_proc(proc, sig, timeout):
    try:
        os.killpg(os.getpgid(proc.pid), sig)
    except (ProcessLookupError, PermissionError) as e:
        dbg(f"killpg: {e}")
        return
    try:
        await asyncio.wait_for(proc.wait(), timeout=timeout)
    except asyncio.TimeoutError:
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
        except Exception: pass
        try:
            await asyncio.wait_for(proc.wait(), timeout=5)
        except Exception: pass
    except Exception:
        pass


async def run_worker_silent(phone, mode, timeout_sec, stop_event, proc_holder):
    """
    worker.py চালায়, আউটপুট শুধু Termux-এ প্রিন্ট করে (user-কে দেখায় না)।
    stop_event সেট হলে সাথে সাথে SIGINT পাঠিয়ে বন্ধ করে।
    """
    if stop_event.is_set():
        return "(শুরুর আগেই বন্ধ)", "stopped", 0

    if not os.path.exists(WORKER_PY):
        return f"❌ worker.py নেই: {WORKER_PY}", "error", 0

    try:
        proc = await asyncio.create_subprocess_exec(
            sys.executable, "-u", WORKER_PY,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,
            start_new_session=True,
        )
    except Exception as e:
        return f"❌ subprocess ব্যর্থ: {e}", "error", 0

    proc_holder["proc"] = proc
    print(f"🚀 [MAIN] worker শুরু (pid={proc.pid}, mode={mode}, phone={phone})", flush=True)

    # stdin-এ শুধু ২টি ইনপুট
    payload = f"{mode}\n{phone}\n"
    print(f"📤 [MAIN→WORKER] stdin = {payload!r}", flush=True)
    try:
        proc.stdin.write(payload.encode())
        await proc.stdin.drain()
        proc.stdin.close()
        print("📤 [MAIN] stdin বন্ধ — আর কোনো ইনপুট নেই", flush=True)
    except Exception as e:
        dbg(f"stdin FAIL: {e}")

    lines_buf = []
    start = asyncio.get_event_loop().time()

    async def reader():
        while True:
            try:
                raw = await proc.stdout.readline()
            except Exception:
                break
            if not raw: break
            line = strip_ansi(raw.decode("utf-8", errors="replace").rstrip("\r\n"))
            if line:
                print(f"[WORKER {phone}] {line}", flush=True)   # ← শুধু Termux
                lines_buf.append(line)
                if len(lines_buf) > 200:
                    del lines_buf[:-200]

    reader_task = asyncio.create_task(reader())
    proc_done   = asyncio.create_task(proc.wait())
    stop_wait   = asyncio.create_task(stop_event.wait())

    status = "success"
    try:
        done, _ = await asyncio.wait(
            [proc_done, stop_wait],
            timeout=timeout_sec,
            return_when=asyncio.FIRST_COMPLETED,
        )

        if stop_wait in done and stop_wait.result():
            status = "stopped"
            print("🛑 [MAIN] user STOP → SIGINT", flush=True)
            await _kill_proc(proc, signal.SIGINT, timeout=20)

        elif proc_done in done:
            rc = proc_done.result()
            if rc != 0:
                status = "error"
                print(f"⚠️ [MAIN] worker exit={rc}", flush=True)
            else:
                print("✅ [MAIN] worker নিজেই শেষ", flush=True)

        else:
            status = "timeout"
            print(f"⏰ [MAIN] {timeout_sec}s শেষ → SIGINT", flush=True)
            await _kill_proc(proc, signal.SIGINT, timeout=20)

    except Exception:
        log("run_worker EXCEPTION:\n" + traceback.format_exc())
        status = "error"
        await _kill_proc(proc, signal.SIGKILL, timeout=5)
    finally:
        stop_wait.cancel()
        reader_task.cancel()
        try: await stop_wait
        except Exception: pass
        try: await reader_task
        except Exception: pass

    elapsed = int(asyncio.get_event_loop().time() - start)
    tail = "\n".join(lines_buf[-50:]) if lines_buf else "(কোনো আউটপুট নেই)"
    return f"[{elapsed}s]\n{tail}", status, elapsed

# ============================================================
# ==================== ইউজার হ্যান্ডলার ======================
# ============================================================
async def u_ping(update, context):
    await update.message.reply_text("🏓 Pong!")

async def u_myid(update, context):
    u = update.effective_user
    await update.message.reply_text(
        f"🆔 `{u.id}`\n👤 @{u.username or 'নেই'}",
        parse_mode="Markdown")

async def u_start(update, context):
    user = update.effective_user
    log(f"/start user={user.id} @{user.username}")
    save_user(user)

    _user_pending.pop(user.id, None)
    uid = str(user.id)
    points = load_json(POINTS_FILE, {})
    first = uid not in points
    if first:
        points[uid] = 1
        save_json(POINTS_FILE, points)

    text = ("🎉 *স্বাগতম!* প্রথমবার ১ পয়েন্ট পেলেন।\n\n" if first
            else f"👋 *আবার স্বাগতম!* পয়েন্ট: *{points[uid]}*\n\n")
    text += "নিচের বাটন থেকে কাজ বেছে নিন 👇"
    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=user_menu())

async def u_menu(update, context):
    q = update.callback_query
    log(f"[USER CB] {q.from_user.id} data={q.data}")
    try: await q.answer()
    except: pass

    try:
        data    = q.data
        chat_id = q.message.chat_id
        uid     = str(q.from_user.id)
        points  = load_json(POINTS_FILE, {})

        if data == "u_home":
            _user_pending.pop(chat_id, None)
            await safe_edit(
                q,
                f"👋 *মেনু* | পয়েন্ট: *{points.get(uid, 0)}*\n\nএকটি অপশন বেছে নিন 👇",
                reply_markup=user_menu())
        elif data == "u_bal":
            await safe_edit(q,
                f"💰 *আপনার পয়েন্ট:* {points.get(uid, 0)}",
                reply_markup=user_back())
        elif data == "u_hist":
            items = load_json(HISTORY_FILE, {}).get(uid, [])
            if not items:
                txt = "📭 কোনো হিস্টোরি নেই।"
            else:
                lines = ["🗂️ *সর্বশেষ ১০টি কাজ:*\n"]
                for i, h in enumerate(items[-10:][::-1], 1):
                    icon = {"success": "✅", "timeout": "⏰",
                            "error": "❌", "stopped": "🛑"}.get(h.get("status"), "•")
                    lines.append(f"{i}. {icon} `{h.get('phone','')}` "
                                 f"| {h.get('status','')} | {h.get('time','')}")
                txt = "\n".join(lines)
            await safe_edit(q, txt, reply_markup=user_back())
        elif data == "u_run":
            if uid in _running_tasks:
                await safe_edit(q,
                    "⚠️ আপনার একটি কাজ ইতিমধ্যে চলছে।\nআগে সেটি শেষ/বন্ধ করুন।",
                    reply_markup=user_back())
                return
            if points.get(uid, 0) < POINT_COST:
                await safe_edit(q,
                    f"❌ পয়েন্ট কম (দরকার {POINT_COST})। অ্যাডমিনের কাছে কিনুন।",
                    reply_markup=user_back())
                return
            _user_pending[chat_id] = {"action": "run"}
            await safe_edit(q,
                "📱 *টার্গেট ফোন নম্বর পাঠান*\nযেমন: `016185940243`\n\nবাতিল: /cancel",
                reply_markup=user_back())
        elif data == "u_contact":
            _user_pending[chat_id] = {"action": "contact"}
            await safe_edit(q,
                "📩 *অ্যাডমিনকে কী বলতে চান?* টাইপ করুন।\nবাতিল: /cancel",
                reply_markup=user_back())

    except Exception:
        log("u_menu EXCEPTION:\n" + traceback.format_exc())


async def u_text(update, context):
    chat_id = update.message.chat_id
    log(f"[u_text] {chat_id} text={update.message.text!r}")
    pending = _user_pending.pop(chat_id, None)
    if not pending: return
    try:
        if pending["action"] == "run":
            await _do_run(update, context)
        elif pending["action"] == "contact":
            await _do_contact(update, context)
    except Exception:
        log("u_text EXCEPTION:\n" + traceback.format_exc())
        try: await update.message.reply_text("⚠️ সমস্যা। /start দিন।")
        except: pass


async def _do_run(update, context):
    user   = update.effective_user
    uid    = str(user.id)
    phone  = update.message.text.strip()
    save_user(user)

    points = load_json(POINTS_FILE, {})
    bal    = points.get(uid, 0)

    if uid in _running_tasks:
        await update.message.reply_text(
            "⚠️ আপনার একটি কাজ ইতিমধ্যে চলছে।", reply_markup=user_menu())
        return
    if bal < POINT_COST:
        await update.message.reply_text(
            "❌ পয়েন্ট শেষ!", reply_markup=user_menu())
        return

    # mode অটো
    if bal > 50:
        mode, timeout_sec, label = 2, 30*60, "FAST (30 min)"
    else:
        mode, timeout_sec, label = 1, 5*60,  "SLOW (5 min)"

    # পয়েন্ট কাটা
    points[uid] -= POINT_COST
    save_json(POINTS_FILE, points)

    # task সেটআপ
    task_id = uuid.uuid4().hex[:8]
    stop_event  = asyncio.Event()
    proc_holder = {}
    _running_tasks[uid] = {
        "task_id": task_id, "stop": stop_event, "proc": proc_holder,
    }

    # user-কে শুধু "পাঠানো হচ্ছে" + Stop button
    msg = await update.message.reply_text(
        f"📤 *আপনার কাজ পাঠানো হয়েছে...*\n\n"
        f"📱 `{phone}`\n"
        f"⚡ *{label}*\n"
        f"💰 বাকি পয়েন্ট: {points[uid]}\n\n"
        f"_কাজ চলছে, শেষ হলে জানানো হবে।_",
        parse_mode="Markdown",
        reply_markup=stop_button(uid, task_id))

    # worker চালাও (silent)
    out, status, duration = await run_worker_silent(
        phone, mode, timeout_sec, stop_event, proc_holder)

    _running_tasks.pop(uid, None)
    add_history(uid, phone, out, status, duration)

    # ফাইনাল status
    status_map = {
        "success": ("✅", "সম্পন্ন"),
        "timeout": ("⏰", "সময় শেষ"),
        "stopped": ("🛑", "আপনি বন্ধ করেছেন"),
        "error":   ("❌", "সমস্যা হয়েছে"),
    }
    icon, label2 = status_map.get(status, ("•", status))

    try:
        await msg.edit_text(
            f"{icon} *{label2}*\n\n"
            f"📱 `{phone}`\n"
            f"⚡ *{label}*\n"
            f"⏱️ সময়: {duration}s",
            parse_mode="Markdown",
            reply_markup=user_menu())
    except Exception as e:
        log(f"final edit FAIL: {e}")


async def u_stop_cb(update, context):
    q = update.callback_query
    data = q.data  # u_stop:UID:TASK_ID
    parts = data.split(":")
    if len(parts) != 3:
        await q.answer()
        return

    _, target_uid, target_task_id = parts
    me = str(q.from_user.id)

    if target_uid != me:
        await q.answer("⛔ এটি আপনার কাজ নয়।", show_alert=True)
        return

    task = _running_tasks.get(me)
    if not task or task.get("task_id") != target_task_id:
        await q.answer("ℹ️ এই কাজ ইতিমধ্যে শেষ।", show_alert=True)
        return

    task["stop"].set()
    proc = task.get("proc", {}).get("proc")
    if proc:
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGINT)
            print(f"🛑 [MAIN] user stop → SIGINT to pid {proc.pid}", flush=True)
        except Exception as e:
            dbg(f"stop SIGINT: {e}")

    await q.answer("🛑 বন্ধ করা হচ্ছে...", show_alert=False)
    try:
        await q.edit_message_text(
            "🛑 *বন্ধ করা হচ্ছে...*\n\nঅনুগ্রহ করে অপেক্ষা করুন।",
            parse_mode="Markdown")
    except Exception:
        pass


async def _do_contact(update, context):
    user = update.effective_user
    save_user(user)
    try:
        await app_user.bot.send_message(
            chat_id=ADMIN_USER_ID,
            text=(f"📩 *নতুন বার্তা*\n"
                  f"👤 {user.username or user.first_name} (`{user.id}`)\n"
                  f"💬 {update.message.text}"),
            parse_mode="Markdown")
    except Exception as e:
        log(f"contact FAIL: {e}")
    await update.message.reply_text("✅ পাঠানো হয়েছে।", reply_markup=user_menu())


async def u_cancel(update, context):
    _user_pending.pop(update.message.chat_id, None)
    await update.message.reply_text("❌ বাতিল।", reply_markup=user_menu())

# ============================================================
# ==================== অ্যাডমিন হ্যান্ডলার ===================
# ============================================================
def is_admin(u): return u.effective_user.id == ADMIN_USER_ID

async def a_ping(update, context):
    await update.message.reply_text("🏓 Admin Pong!")

async def a_start(update, context):
    if not is_admin(update):
        await update.message.reply_text("⛔ অ্যাডমিন নন।")
        return
    _admin_pending.pop(update.message.chat_id, None)
    await update.message.reply_text(
        "👑 *অ্যাডমিন প্যানেল*\nনিচের বাটন ব্যবহার করুন 👇",
        parse_mode="Markdown", reply_markup=admin_menu())


async def a_menu(update, context):
    q = update.callback_query
    try: await q.answer()
    except: pass
    if not is_admin(update):
        await safe_edit(q, "⛔"); return

    data, chat_id = q.data, q.message.chat_id
    try:
        if data == "a_home":
            _admin_pending.pop(chat_id, None)
            await safe_edit(q, "👑 *অ্যাডমিন প্যানেল*", reply_markup=admin_menu())

        elif data == "a_users":
            pts = load_json(POINTS_FILE, {})
            usr = load_json(USERS_FILE, {})
            if not pts:
                txt = "📭 কোনো ইউজার নেই।"
            else:
                lines = ["👥 *ইউজার তালিকা:*\n"]
                for u, p in pts.items():
                    uname = usr.get(u, {}).get("username", "")
                    disp  = f"@{uname}" if uname else u
                    lines.append(f"• {disp} → *{p}* পয়েন্ট (`{u}`)")
                txt = "\n".join(lines)
            await safe_edit(q, txt, reply_markup=admin_back())

        elif data == "a_history":
            h = load_json(HISTORY_FILE, {})
            if not h:
                txt = "📭 কোনো হিস্টোরি নেই।"
            else:
                lines = ["📊 *ইউজার হিস্টোরি সারসংক্ষেপ:*\n"]
                for u, items in h.items():
                    lines.append(f"• `{u}` → {len(items)}টি রান")
                txt = "\n".join(lines)
            await safe_edit(q, txt, reply_markup=admin_back())

        elif data in ("a_add", "a_remove"):
            _admin_pending[chat_id] = {"action": data}
            verb = "দিতে" if data == "a_add" else "কমাতে"
            await safe_edit(q,
                f"🆔 *কাকে পয়েন্ট {verb} চান?*\n\n"
                f"`@username` অথবা `user_id` পাঠান।\nবাতিল: /cancel",
                reply_markup=admin_back())
    except Exception:
        log("a_menu EXCEPTION:\n" + traceback.format_exc())


async def a_text(update, context):
    if not is_admin(update): return
    chat_id = update.message.chat_id
    pending = _admin_pending.get(chat_id)
    if not pending: return

    txt = update.message.text.strip()

    # ধাপ ১: target (username বা user_id)
    if "uid" not in pending:
        target_uid = resolve_target(txt)
        if not target_uid:
            await update.message.reply_text(
                f"❌ `{txt}` কে পাওয়া যায়নি।\n"
                f"_ইউজারকে আগে `/start` করতে হবে।_",
                parse_mode="Markdown")
            return

        # চেক করে থাকলে তার real username
        usr = load_json(USERS_FILE, {}).get(target_uid, {})
        uname = usr.get("username", "")
        display = f"@{uname}" if uname else target_uid

        pending["uid"] = target_uid
        await update.message.reply_text(
            f"🎯 Target: *{display}*\n"
            f"🆔 `{target_uid}`\n\n"
            f"🔢 *পরিমাণ লিখুন।* বাতিল: /cancel",
            parse_mode="Markdown", reply_markup=admin_back())
        return

    # ধাপ ২: পরিমাণ
    if not txt.isdigit():
        await update.message.reply_text("❌ সংখ্যা দিন।")
        return

    amt    = int(txt)
    uid    = pending["uid"]
    action = pending["action"]
    _admin_pending.pop(chat_id, None)

    points = load_json(POINTS_FILE, {})
    if action == "a_add":
        points[uid] = points.get(uid, 0) + amt
        note = f"🎁 অ্যাডমিন আপনাকে {amt} পয়েন্ট দিয়েছেন।\nমোট: {points[uid]}"
    else:
        points[uid] = max(0, points.get(uid, 0) - amt)
        note = f"📉 অ্যাডমিন আপনার {amt} পয়েন্ট কেটেছেন।\nমোট: {points[uid]}"
    save_json(POINTS_FILE, points)

    usr = load_json(USERS_FILE, {}).get(uid, {})
    display = f"@{usr.get('username')}" if usr.get("username") else uid

    await update.message.reply_text(
        f"✅ {display} (`{uid}`) → *{points[uid]}* পয়েন্ট",
        parse_mode="Markdown", reply_markup=admin_menu())

    # ইউজারকে notify
    try:
        await app_user.bot.send_message(chat_id=int(uid), text=note)
    except Exception as e:
        log(f"notify user {uid} FAIL: {e}")


async def a_cancel(update, context):
    _admin_pending.pop(update.message.chat_id, None)
    await update.message.reply_text("❌ বাতিল।", reply_markup=admin_menu())


async def a_addpoints_cmd(update, context):
    """/addpoints @username 10   অথবা   /addpoints 5610589273 10"""
    if not is_admin(update): return
    if len(context.args) != 2 or not context.args[1].isdigit():
        await update.message.reply_text(
            "ব্যবহার: `/addpoints @username 10` অথবা `/addpoints 5610589273 10`",
            parse_mode="Markdown")
        return

    target_uid = resolve_target(context.args[0])
    if not target_uid:
        await update.message.reply_text("❌ ইউজার পাওয়া যায়নি।")
        return

    amt = int(context.args[1])
    points = load_json(POINTS_FILE, {})
    points[target_uid] = points.get(target_uid, 0) + amt
    save_json(POINTS_FILE, points)

    usr = load_json(USERS_FILE, {}).get(target_uid, {})
    display = f"@{usr.get('username')}" if usr.get("username") else target_uid

    await update.message.reply_text(
        f"✅ {display} (`{target_uid}`) → *{points[target_uid]}* পয়েন্ট",
        parse_mode="Markdown")

    try:
        await app_user.bot.send_message(
            chat_id=int(target_uid),
            text=f"🎁 অ্যাডমিন আপনাকে {amt} পয়েন্ট দিয়েছেন।\nমোট: {points[target_uid]}")
    except Exception:
        pass


async def a_balance_cmd(update, context):
    """/balance @username   → ওই ইউজারের পয়েন্ট"""
    if not is_admin(update): return
    if not context.args:
        await update.message.reply_text("ব্যবহার: `/balance @username`",
                                        parse_mode="Markdown"); return

    target_uid = resolve_target(context.args[0])
    if not target_uid:
        await update.message.reply_text("❌ ইউজার পাওয়া যায়নি।"); return

    points = load_json(POINTS_FILE, {})
    usr = load_json(USERS_FILE, {}).get(target_uid, {})
    display = f"@{usr.get('username')}" if usr.get("username") else target_uid

    await update.message.reply_text(
        f"💰 {display} (`{target_uid}`) → *{points.get(target_uid, 0)}* পয়েন্ট",
        parse_mode="Markdown")

# ==================== বিল্ড ====================
def build_user_app():
    app = ApplicationBuilder().token(USER_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start",  u_start))
    app.add_handler(CommandHandler("cancel", u_cancel))
    app.add_handler(CommandHandler("ping",   u_ping))
    app.add_handler(CommandHandler("myid",   u_myid))
    app.add_handler(CallbackQueryHandler(u_stop_cb, pattern=r"^u_stop:"))
    app.add_handler(CallbackQueryHandler(u_menu))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, u_text))
    return app

def build_admin_app():
    app = ApplicationBuilder().token(ADMIN_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start",     a_start))
    app.add_handler(CommandHandler("cancel",    a_cancel))
    app.add_handler(CommandHandler("ping",      a_ping))
    app.add_handler(CommandHandler("addpoints", a_addpoints_cmd))
    app.add_handler(CommandHandler("balance",   a_balance_cmd))
    app.add_handler(CallbackQueryHandler(a_menu))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, a_text))
    return app

# ==================== main ====================
async def main():
    global app_user, app_admin

    print("=" * 55)
    print(f"📂 WORKER_PY = {WORKER_PY}")
    print(f"✅ আছে?     = {os.path.exists(WORKER_PY)}")
    print("=" * 55)

    app_user  = build_user_app()
    app_admin = build_admin_app()
    await app_user.initialize()
    await app_admin.initialize()

    try:
        me_u = await app_user.bot.get_me()
        log(f"USER  @{me_u.username} (id={me_u.id})")
    except Exception as e:
        log(f"❌ USER getMe FAIL: {e}"); raise
    try:
        me_a = await app_admin.bot.get_me()
        log(f"ADMIN @{me_a.username} (id={me_a.id})")
    except Exception as e:
        log(f"❌ ADMIN getMe FAIL: {e}"); raise

    await app_user.start()
    await app_admin.start()
    await app_user.updater.start_polling(
        drop_pending_updates=True,
        allowed_updates=["message", "callback_query"])
    await app_admin.updater.start_polling(
        drop_pending_updates=True,
        allowed_updates=["message", "callback_query"])

    print("\n" + "=" * 55)
    print(f"✅ USER  @{me_u.username}")
    print(f"✅ ADMIN @{me_a.username}")
    print("=" * 55)
    print("User: /start  |  Admin: /start")
    print("থামাতে: Ctrl+C")
    print("=" * 55 + "\n")

    stop = asyncio.Event()
    try:
        loop = asyncio.get_running_loop()
        for s in (signal.SIGINT, signal.SIGTERM):
            try: loop.add_signal_handler(s, stop.set)
            except: pass
    except: pass

    try:
        await stop.wait()
    except (asyncio.CancelledError, KeyboardInterrupt):
        pass

    print("\n🛑 বন্ধ হচ্ছে...")
    for name, app in (("user", app_user), ("admin", app_admin)):
        try:
            if app.updater and app.updater.running:
                await app.updater.stop()
            await app.stop()
            await app.shutdown()
        except Exception as e:
            log(f"shutdown {name}: {e}")
    print("✅ বন্ধ।")

if __name__ == "__main__":
    try:
        check_and_create_lock()
    except SystemExit:
        raise
    except Exception as e:
        print(f"lock চেক ব্যর্থ: {e}")

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 বাই!")
    finally:
        remove_lock()
