from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, RadioField, \
    TextAreaField, FloatField, HiddenField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Optional, InputRequired, Email, StopValidation
from wtforms import widgets
from wtforms.compat import string_types


class FarmerForm(FlaskForm):
    farmerlocation = StringField("Where is your farm?", validators=[InputRequired()])
    help = StringField("What do you need with?")
    details = StringField("Additional details")
    when = StringField("When do you need help?")
    phone = StringField("Phone number")
    email = EmailField("Your E-Mail address?")

    # hidden fields: used to get data from places API and store it in db
    formatted_address = HiddenField()
    lat = HiddenField()
    lng = HiddenField()

    farmerSubmit = SubmitField("Submit")


class HelperForm(FlaskForm):
    helperlocation = StringField("Where do you live?", validators=[InputRequired()])

    helperSubmit = SubmitField("Submit")


class VerficationForm(FlaskForm):
    verificationCode = StringField("Verification Code")
    submit = SubmitField("Verify!")