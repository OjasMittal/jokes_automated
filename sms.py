import os
import requests
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

def send_sms(to_phone, joke):
    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = f"message={joke}&language=english&route=q&numbers={to_phone}"
    headers = {
        'authorization': os.getenv("SMS_AUTH_KEY"),
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)