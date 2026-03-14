from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Load Telegram token from environment variable
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables")

URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# Root route for testing in browser
@app.route("/")
def home():
    return "Flask Telegram Bot is running ✅"

# Telegram webhook route
@app.route("/webhook", methods=["POST"])
def telegram_bot():
    data = request.json
    if not data or "message" not in data:
        return "ok"

    chat_id = data["message"]["chat"]["id"]
    message = data["message"]["text"].lower()

    # Simple rule-based responses
    if "hello" in message:
        reply = "Hello! How can I help you?"
    elif "price" in message:
        reply = "Product price is $10"
    elif "order" in message:
        reply = "Please send your order ID"
    else:
        reply = "Sorry, I did not understand."

    # Send reply to Telegram
    requests.post(URL, json={"chat_id": chat_id, "text": reply})

    return "ok"
