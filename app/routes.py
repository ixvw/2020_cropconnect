from app import app
from flask import Flask, render_template, redirect, url_for, request

from app.forms import *

from app.util.sendgridMail import sendgridMail

@app.route('/', methods=['GET', 'POST'])
def index():
    farmerform = FarmerForm()
    helperform = HelperForm()

    if helperform.validate_on_submit():
        if helperform.helperlocation.data != "":
            return("helper provided his data")

    if farmerform.validate_on_submit():
        if farmerform.farmerlocation.data != "":
            # TODO: Write farm info to db (table of not validated farms), create verification code and send e-mail with
            # verification code / link to the given e-mail adress

            # TODO: insted of "0000" send real idToValidate to /validate_email

            idToValidate = "00000"

            sendgridMail(idToValidate, farmerform.email.data)

            return redirect(url_for("validate_email", messages=idToValidate))

    return render_template('index.html', farmerform=farmerform, helperform=helperform)


@app.route('/validate_email', methods=['GET', 'POST'])
def validate_email():
    messages = request.args["messages"]

    return("farmer provided his data -> ask him to validate his email. idToValidate = {}".format(messages))

