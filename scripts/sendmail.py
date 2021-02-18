import smtplib
import os
import rssgetmenu

gmail_user = os.environ['GMAIL_ADDRESS'].strip("\"")
gmail_password = os.environ['GMAIL_PASSWORD'].strip("\"")

to = os.environ["SEND_MENU_TO"].strip("\"").split(",")
subject = 'Dagens mat'
body = "Hello World!"

email_text = "\
From: {}\n\
To: {}\n\
Subject: {}\n\
\
{}\
".format(gmail_user, ", ".join(to), subject, body)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail(gmail_user, to, email_text)
server.close()

print('Email sent!')