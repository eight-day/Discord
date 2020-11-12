from requests import exceptions, Session
from json import dumps
from random import choice
try:
	import getpass
	gpass = True
except ImportError:
	print('[1] getpass not installed, will not attempt to mask your password.')
	gpass = False

try:
	username = input('Usename[email]: ')
	password = getpass.getpass() if gpass else input('Password: ')
	
	print(f'[!] Attempting with: {username} and given password.')
	with Session() as Extractor:
		try:
			Extractor.get('https://discord.com')
			print("[!] Connection established.")
			
			login_data = dumps({
				'captcha_key': '',
				'email': username,
				'login_source': '',
				'password': password,
				'undelete': 'false'
			})
			Extractor.headers.update({
				'Content-Type': 'application/json',
				'User-Agent': choice([
					'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1,'
					'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko; googleweblight) Chrome/38.0.1025.166 Mobile Safari/535.19',
					'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
				])
			})
			
			Extracted = Extractor.post("https://discord.com/api/v6/auth/login", data=login_data).json()
			print("{}".format('[1] Failed to extract token' if 'token' not in Extracted else '[+] Token: {}'.format(Extracted['token'])))
		except Exception as Error:
			print(f"[1] {Error}")
			exit(1)
except (KeyboardInterrupt, EOFError):
	print('\n[0] Interrupt caught, exiting.')
	exit(0)
