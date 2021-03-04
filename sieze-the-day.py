import requests

token = input("Token: ")

light_header_payload = {
    'Authorization': token,
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'Content-Length': '17',
}

dark_header_payload = {
    'Authorization': token,
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'Content-Length': '16',
}

x = requests.get('https://discordapp.com/')
cookie_payload = {
    '__cfduid': x.cookies['__cfduid'],
}

light_payload = {
    'theme': 'light',
}

dark_payload = {
    'theme': 'dark',
}


while True:
    r = requests.patch('https://discordapp.com/api/v6/users/@me/settings', json=light_payload, headers=light_header_payload, cookies=cookie_payload)
    r = requests.patch('https://discordapp.com/api/v6/users/@me/settings', json=dark_payload, headers=dark_header_payload, cookies=cookie_payload)
    if(r.status_code == 200):
        print("[*] Theme Flickered Successfully.\n")
    elif(r.status_code == 401):
        print("[!] Error. Invalid Token.\n")
    else:
        print("[!] Error. Unknown Cause.\n")
