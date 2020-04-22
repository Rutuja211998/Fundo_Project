"""
This file contains SMTP mail class throgh which we are going to send token on mail.
Author: Rutuja Tikhile.
Date:9/3/2020
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()


class SMTP_Mail:

    def do_mailing(self, message, user_email):
        # create message object instance
        msg = MIMEMultipart()

        # message = "Click on the link below to confirm your registration: http://127.0.0.1/activate/?token='" + token + "'"

        # setup the parameters of the message
        password = os.getenv('password')
        msg['From'] = os.getenv('from')
        msg['To'] = user_email
        msg['Subject'] = "Link"

        # add in the message body
        msg.attach (MIMEText (message, 'plain'))

        # create server
        server = smtplib.SMTP ('smtp.gmail.com: 587')

        server.starttls ()

        # Login Credentials for sending the mail
        server.login (msg['From'], password)

        # send the message via the server.
        server.sendmail (msg['From'], msg['To'], msg.as_string ())
        server.quit ()
