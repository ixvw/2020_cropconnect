from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, RadioField, \
    TextAreaField, FloatField, HiddenField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Optional, InputRequired, Email, StopValidation
from wtforms import widgets
from wtforms.compat import string_types

from flask_babel import _
from flask_babel import lazy_gettext as _l


class FarmerForm(FlaskForm):
    farmerlocation = StringField(_l("Where is your farm?"), render_kw={"placeholder": _l("start typing...")}, validators=[InputRequired()])
    help = StringField(_l("Help needed?"))
    details = StringField(_l("Additional details"))
    when = StringField(_l("When?"))
    phone = StringField(_l("Phone number"))
    email = EmailField(_l("E-Mail:"))

    # hidden fields: used to get data from places API and store it in db
    formatted_address = HiddenField()
    lat = HiddenField()
    lng = HiddenField()

    farmerSubmit = SubmitField(_l("Submit"))


class HelperForm(FlaskForm):
    helperlocation = StringField(_l("Where do you live?"), render_kw={"placeholder": _l("start typing...")}, validators=[InputRequired()])

    helperSubmit = SubmitField(_l("Submit"))


class VerficationForm(FlaskForm):
    verificationCode = StringField(_l("Please enter the verification code we sent to your E-Mail address"))
    submit = SubmitField(_l("Verify!"))
