import smtplib
import os
from dotenv import load_dotenv


load_dotenv()
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(name,to_email, joke):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_LOGIN, EMAIL_PASSWORD)
            subject = "Here's a Joke for You!"
            message = f"Subject: {subject}\n\nHey {name},\n\nAs promised, here's your lame joke:\n\n{joke} :)\n\nThanks for sparing your precious time in filling out the survey.\nRegards,\nTeam - Jokes :)"
            server.sendmail(EMAIL_LOGIN, to_email, message)
    except Exception as e:
        print(f"Error in send_email: {e}")
        raise