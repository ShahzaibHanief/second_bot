from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route("/webhook", methods=["POST"])
def telegram_bot():

    data = request.json

    message = data["message"]["text"]
    chat_id = data["message"]["chat"]["id"]

    message = message.lower()

    if "hello" in message:
        reply = "Hello! How can I help you?"

    elif "price" in message:
        reply = "Product price is $10"

    elif "order" in message:
        reply = "Please send your order ID"

    else:
        reply = "Sorry, I did not understand."

    requests.post(URL, json={
        "chat_id": chat_id,
        "text": reply
    })

    return "ok"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Railway gives PORT dynamically
    app.run(host="0.0.0.0", port=port)       # Bind to all IPs
