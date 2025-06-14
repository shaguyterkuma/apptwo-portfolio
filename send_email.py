import os
import smtplib, ssl
from smtplib import SMTP_SSL

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "shaguyterkuma@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "shaguyterkuma@gmail.com"
    my_context = ssl._create_unverified_context()

    email_message = f"""\
Subject: Message from Portfolio Contact Form

{message}
"""

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, email_message)
