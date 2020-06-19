from app import app
from flask import Flask, flash, render_template, redirect, url_for, request
from random import randint
import uuid

from app.forms import *

from app.database import db, Farm

from app.util.sendgridMail import sendgridMail, sendgridMailDeletion

from geopy import distance

from app.util.orm import orm_object_as_dict
from app.util.allowedImg import allowedImg

from app import babel
from flask_babel import _

from app.util.imgPath import imgPath

from werkzeug.utils import secure_filename

import os


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET', 'POST'])
def index():
    farmerform = FarmerForm()
    helperform = HelperForm()

    if farmerform.validate_on_submit():
        if farmerform.farmerlocation.data != "":

            filename = secure_filename(farmerform.photo.data.filename)

            if filename is not None:
                # check provided img before storing it!
                if allowedImg(filename):
                    farmerform.photo.data.save(imgPath(filename))
                else:
                    flash(_("The file you want to upload does not seem to be an image"))

                farm = Farm(email=farmerform.email.data, formatted_address=farmerform.formatted_address.data,
                        help=farmerform.help.data, details=farmerform.details.data, when=farmerform.when.data,
                        phone=farmerform.phone.data, lat=farmerform.lat.data, lng=farmerform.lng.data, imgname=filename)
            else:
                farm = Farm(email=farmerform.email.data, formatted_address=farmerform.formatted_address.data,
                            help=farmerform.help.data, details=farmerform.details.data, when=farmerform.when.data,
                            phone=farmerform.phone.data, lat=farmerform.lat.data, lng=farmerform.lng.data)

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
                return render_template("verified.html", verificationresult=_("verification successful!"))
            else:
                return render_template("verified.html", verificationresult=_("Wrong verification code!"))

        return render_template('verification.html', form=form)

    else:
        # getParam is not None, i.e. user clicked on verification link in email -> verify farm and display
        # success, display an error if not found or inform that farm has already been validated
        farm = Farm().query.filter(Farm.validationId == getParamValidation).first()

        if farm.verificationCode == getParamVerification:
            farm.verified = True
            db.session.commit()
            return render_template("verified.html", verificationresult=_("verification successful!"))

        else:
            return render_template("verified.html", verificationresult=_("Something went wrong...! Try again"))


@app.route('/farms', methods=['GET', 'POST'])
def farms():
    helper_lat = request.args.get("lat", None)
    helper_lng = request.args.get("lng", None)

    if helper_lat is not None:
        # take lat and long of helper adress as input
        coords_origin = (helper_lat, helper_lng)

        # query for farms
        farmresults = Farm().query.filter(Farm.verified == True).all()

        farmlist = []

        # calculate the distance to the helper for each farm
        # also: extract ZIP + City from formatted_address to show in list of farms
        for farm_orm in farmresults:
            farm = orm_object_as_dict(farm_orm)
            coords_farm = (farm["lat"], farm["lng"])
            dist = distance.vincenty(coords_origin, coords_farm).km

            farm["distance"] = dist

            split_address = farm["formatted_address"].split(",")
            # formatted_address should always look like:
            # ETH Zürich Hauptgebäude, Rämistrasse 101, 8092 Zürich, Schweiz
            # hence we need to use the penultimate entry of the list
            # maybe in the future we need to check where the string starts with a number and use that element.

            farm["ZipCity"] = split_address[-2]

            farmlist.append(farm)

        # sort farms from nearest to farthest
        farms = sorted(farmlist, key=lambda k: k["distance"])

        return render_template("farms.html", farms=farms)

    return("uups - something went wrong")


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html")


@app.route("/deletion", methods=["GET", "POST"])
def deletion():
    idToDelete = request.args.get("farmid", None)

    farm = Farm().query.filter(Farm.id == idToDelete).first()

    # create deletionId and deletionCode
    deletionCode = randint(100000, 999999)
    farm.deletionCode = deletionCode

    deletionId = str(uuid.uuid4())
    farm.deletionId = deletionId

    db.session.commit()

    # send to user via e-mail
    sendgridMailDeletion(deletionCode, deletionId, farm.email)

    # redirect
    return redirect("deletefarm?farmid="+idToDelete)


@app.route("/deletefarm", methods=["GET", "POST"])
def deletefarm():
    idToDelete = request.args.get("farmid", None)
    getParamValidation = request.args.get("deletionId", None)
    getParamVerification = request.args.get("deletionCode", None)

    if getParamValidation is None:
        # getParam is None if user did not come via delete link in email, thus ask to type deletion code
        farm = Farm().query.filter(Farm.id == idToDelete).first()

        deletionCode = farm.deletionCode

        form = FarmDeletionVerificationForm()

        if form.validate_on_submit():
            if form.verificationCode.data == deletionCode:
                db.session.delete(farm)
                db.session.commit()
                return render_template("verified.html", verificationresult=_("farm deleted successfully!"))
            else:
                return render_template("verified.html", verificationresult=_("Wrong verification code!"))

        return render_template('verification.html', form=form)

    else:
        # getParam is not None, i.e. user clicked on deletion link in email -> delete farm
        # success, display an error if not found
        farm = Farm().query.filter(Farm.deletionId == getParamValidation).first()

        if farm is None:
            return render_template("verified.html", verificationresult=_("farm not found! Probably it was already deleted"))

        if farm.deletionCode == getParamVerification:
            db.session.delete(farm)
            db.session.commit()
            return render_template("verified.html", verificationresult=_("farm deleted successfully!"))

        else:
            return render_template("verified.html", verificationresult=_("Something went wrong...! Try again"))




# currently unused, since imgs are stored and saved in /static
@app.context_processor
def utility_processor():
    def imgPathJinja(filename):
        print(imgPath(filename))
        return imgPath(filename)
    return dict(imgPathJinja=imgPathJinja)

# used to display the img out of farmimgs folder in static
@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='farmimgs/' + filename), code=301)

