import smtplib, ssl, certifi
from smtplib import SMTP_SSL

host = "smtp.gmail.com"
port = 465


username = "shaguyterkuma@gmail.com"
password = "rnlp yanx fthj kwxw"

receiver = "shaguyterkuma@gmail.com"
my_context = ssl._create_unverified_context()

message = """\
Subject: Hi!

"""

with smtplib.SMTP_SSL(host,port,context=my_context) as server:
    server.login(username,password)
    server.sendmail(username,receiver,message)