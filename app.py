from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__)

# 🔴 ضع بيانات البوت هنا
BOT_TOKEN = "8073621434:AAH-Bm7fVfkl-1VeGZGE_oyBLGr2tSCNnhE"
CHAT_ID = "703015262"


def send_to_telegram(text):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        data = {
            "chat_id": CHAT_ID,
            "text": text
        }

        response = requests.post(url, data=data)

        print("Telegram response:", response.text)

    except Exception as e:
        print("Error sending to Telegram:", e)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=["POST"])
def send():

    name = request.form.get("name")
    phone = request.form.get("phone")
    message = request.form.get("message")

    text = f"""
📥 رسالة جديدة من الموقع

👤 الاسم: {name}
📱 الهاتف: {phone}
💬 الرسالة: {message}
"""

    send_to_telegram(text)

    return "<h2 style='text-align:center;font-family:Arial;'>تم الإرسال بنجاح ✅</h2>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)