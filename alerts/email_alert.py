import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER = os.getenv("RECEIVER_EMAIL")


class EmailAlert:

    def send(self, subject, body):

        msg = MIMEMultipart()

        msg["From"] = EMAIL
        msg["To"] = RECEIVER
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(EMAIL, PASSWORD)

        server.send_message(msg)

        server.quit()

        print("✅ Email Sent")