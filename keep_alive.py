from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return "Anti-Spam#4950 is running!\nAnti Spam is a good discord bot if you want a chill server to relax in."


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()