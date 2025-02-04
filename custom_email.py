import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(to_email, content, name="friend"):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_LOGIN, EMAIL_PASSWORD)
            formatted_content = content.replace("\n", "<br>")
            subject = "Knock Knock ! Say Who is it?"
            html_body = f"""
            <html>
            <body>
                <p>Hi,</p>
                <p>Thanks for your response!</p>
                <p><b style="font-size: 20px;">{formatted_content}</b></p>
            </body>
            </html>
            """
            
            msg = MIMEMultipart("alternative")
            msg["Subject"] = subject
            msg["From"] = EMAIL_LOGIN
            msg["To"] = to_email
            msg.attach(MIMEText(html_body, "html"))
            
            server.sendmail(EMAIL_LOGIN, to_email, msg.as_string())
    except Exception as e:
        print(f"Error in send_email: {e}")
        raise