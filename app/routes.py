from app import app
from flask import Flask, render_template, redirect, url_for, request
from random import randint
import uuid

from app.forms import *

from app.database import db, Farm

from app.util.sendgridMail import sendgridMail

from geopy import distance


@app.route('/', methods=['GET', 'POST'])
def index():
    farmerform = FarmerForm()
    helperform = HelperForm()

    if farmerform.validate_on_submit():
        if farmerform.farmerlocation.data != "":
            # TODO: Write farm info to db (table of not validated farms), create verification code and send e-mail with
            # verification code / link to the given e-mail adress
            farm = Farm(email=farmerform.email.data, farmerlocation=farmerform.farmerlocation.data,
                        help=farmerform.help.data, details=farmerform.details.data, when=farmerform.when.data,
                        phone=farmerform.phone.data)

            verificationCode = randint(100000, 999999)
            farm.verificationCode = verificationCode

            idToValidate = str(uuid.uuid4())
            farm.validationId = idToValidate

            db.session.add(farm)
            db.session.commit()

            sendgridMail(verificationCode, idToValidate, farmerform.email.data)

            return redirect(url_for("validate_email", messages=idToValidate))

    return render_template('index.html', farmerform=farmerform, helperform=helperform)


@app.route('/validate_email', methods=['GET', 'POST'])
def validate_email():
    idToValidate = request.args.get("messages", None)
    getParamValidation = request.args.get("validationId", None)
    getParamVerification = request.args.get("verification", None)

    if getParamValidation is None:
        # getParam is None if user did not come via verification link in email, thus ask to type verification code
        farm = Farm().query.filter(Farm.validationId == idToValidate).first()

        verificationCode = farm.verificationCode

        form = VerficationForm()

        if form.validate_on_submit():
            if form.verificationCode.data == verificationCode:
                farm.verified = True
                db.session.commit()
                return("verification successful!")
            else:
                return("Wrong verification code!")


        return render_template('verification.html', form=form)

    else:
        # getParam is not None, i.e. user clicked on verification link in email -> verify farm and display
        # success, display an error if not found or inform that farm has already been validated
        farm = Farm().query.filter(Farm.validationId == getParamValidation).first()

        if farm.verificationCode == getParamVerification:
            farm.verified = True
            db.session.commit()
            return ("verification successful!")

        else:
            return ("Wrong verification code!")

    return("farmer provided his data -> ask him to validate his email. idToValidate = {}".format(messages))

@app.route('/farms', methods=['GET', 'POST'])
def farms():
    helper_lat = request.args.get("lat", None)
    helper_lng = request.args.get("lng", None)

    if helper_lat is not None:
        print(helper_lat)
        print(helper_lng)
        # take lat and long of helper adress as input
        coords_origin = (helper_lat, helper_lng)

        # query for farms
        farms = []

        # calculate the distance to the helper for each farm
        for farm in farms:
            farm_lat = 0
            farm_lng = 0

            coords_farm = (farm_lat, farm_lng)
            dist = distance.vincenty(coords_origin, coords_farm).km

        # sort farms from nearest to farthest

        return("hello farms!")

    return("uups - something went wrong")
