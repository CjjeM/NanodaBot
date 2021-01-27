from flask import Flask, request, abort
from threading import Thread
from replit import db

app = Flask('')

@app.route('/')
def home():
    return "Oogabooga"

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("Webhook received")
        db["receive_webhook"] = request.json
        return 'success', 200
    else:
        abort(400)

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()