from flask import Flask, request, jsonify
import smtplib
import random
from jokes import jokes
import os
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

@app.route('/')
def index():
    return "Welcome to the Joke API! Use the '/send-joke' endpoint to send a joke."

@app.route('/send-joke', methods=['POST'])
def send_joke():
    data = request.json

    if not data:
        return jsonify({"error": "No data received"}), 400

    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    joke = data.get("joke")

    if not (name and email and joke):
        return jsonify({"error": "Missing required fields"}), 400
    try:
        send_email(name, email, joke)
    except Exception as e:
        return jsonify({"error": f"Failed to send email: {e}"}), 500
    # try:
    #     send_sms(phone, joke)
    # except Exception as e:
    #     return jsonify({"error": f"Failed to send SMS: {e}"}), 500

    return jsonify({"message": f"Joke sent to {name} successfully!"}), 200

def send_email(name,to_email, joke):
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_LOGIN, EMAIL_PASSWORD)
        subject = "Here's a Joke for You!"
        message = f"Subject: {subject}\n\nHey {name},\n\nAs promised, here's your lame joke:\n\n{joke} :)\n\nThanks for sparing your precious time in filling out the survey.\nRegards,\nYagyansh Mittal"
        server.sendmail(EMAIL_LOGIN, to_email, message)

def send_sms(to_phone, joke):
    import requests
    
    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = f"message={joke}&language=english&route=q&numbers={to_phone}"
    headers = {
        'authorization': os.getenv("SMS_AUTH_KEY"),
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
