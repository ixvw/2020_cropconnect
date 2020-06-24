# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from flask_babel import _

from app import app

def sendgridMail(verificationCode, idToValidate, toEmail):
    host = "cropconnect.ch/"
    if app.config["LOCAL"] == "True":
        host = "localhost:5000/"

    message = Mail(
        from_email='hello@cropconnect.world ',
        to_emails=toEmail,
        subject=_('Cropconnect Verficiation Code'),
        html_content=_("Your cropconnect verification code is: %(vericode)s <br>"
                     "or click the link: "
                     "https://" + host + "validate_email?validationId=%(idToValidate)s&"
                     "verification=%(vericode)s", vericode=verificationCode, idToValidate=idToValidate))

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
    except Exception as e:
        print(e)
        print(e.body)

def sendgridMailDeletion(deletionCode, deletionId, toEmail):
    message = Mail(
        from_email='hello@cropconnect.world ',
        to_emails=toEmail,
        subject=_("Cropconnect Farm Deletion Code"),
        html_content=_("Your cropconnect farm deletion code is: %(vericode)s <br>"
                     "or click the link: "
                     "http://cropconnect.ch/deletefarm?deletionId=%(idToValidate)s&"
                     "deletionCode=%(vericode)s", vericode=deletionCode, idToValidate=deletionId))

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
    except Exception as e:
        print(e)
        print(e.body)

def sendgridMailReport(idToReport):
    message = Mail(
        from_email='hello@cropconnect.world',
        to_emails='cropconnext@gmail.com',
        subject="Cropconnect Farm REPORTED: " + idToReport,
        html_content="The farm {} seems to be abusing cropconnect. Better check it out!".format(idToReport))

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
        print(e.body)