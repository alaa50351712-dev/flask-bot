from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)

# ضع توكن البوت هنا
BOT_TOKEN = "8073621434:AAH-Bm7fVfkl-1VeGZGE_oyBLGr2tSCNnhE"
CHAT_ID = "703015262"


def send_to_bot(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=["POST"])
def send():

    name = request.form.get("name")
    pubg_id = request.form.get("pubg_id")
    uc = request.form.get("uc")

    text = f"""
🎮 NEW REQUEST

👤 Name: {name}
🆔 PUBG ID: {pubg_id}
💰 UC: {uc}
"""

    send_to_bot(text)

    return render_template("done.html")


if __name__ == "__main__":
    app.run(debug=True)
