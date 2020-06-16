# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from app import babel
from flask_babel import _

def sendgridMail(verificationCode, idToValidate, toEmail):
    message = Mail(
        from_email='hello@cropconnect.world ',
        to_emails=toEmail,
        subject=_('Cropconnect Verficiation Code'),
        html_content=_("Your cropconnect verification code is: %(vericode)s <br>"
                     "or click the link: "
                     "http://cropconnect.ch/validate_email?validationId=%(idToValidate)s&"
                     "verification=%(vericode)s", vericode=verificationCode, idToValidate=idToValidate))

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
        print(e.body)