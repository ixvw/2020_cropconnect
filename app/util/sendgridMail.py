# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def sendgridMail(verificationCode, toEmail):
    message = Mail(
        from_email='hello@cropconnect.world ',
        to_emails=toEmail,
        subject='Cropconnect Verficiation Code',
        html_content="Your cropconnect verification code is: {}".format(verificationCode))

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
        print(e.body)