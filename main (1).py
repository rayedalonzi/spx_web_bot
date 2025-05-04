import os
import time
import requests
from threading import Thread
from flask import Flask

app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def run_bot():
    while True:
        send_message("SPX تم رصد كسر منطقة مقاومة")
        time.sleep(3600)

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == '__main__':
    Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=10000)
