from flask import Flask, request, render_template
import requests

app = Flask(__name__)

BOT_TOKEN = "8073621434:AAH-Bm7fVfkl-1VeGZGE_oyBLGr2tSCNnhE"
CHAT_ID = "703015262"

def send(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=["POST"])
def send_form():

    name = request.form.get("name")
    pubg_id = request.form.get("pubg_id")
    uc = request.form.get("uc_amount")

    text = f"""
🎮 PUBG REQUEST

👤 الاسم: {name}
🆔 ID: {pubg_id}
💰 UC: {uc}
"""

    send(text)

    return "<h2 style='text-align:center'>تم الإرسال ✅</h2>"


if __name__ == "__main__":
    app.run(debug=True)