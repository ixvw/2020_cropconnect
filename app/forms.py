from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, HiddenField, ValidationError, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Optional, InputRequired, Email, StopValidation
from wtforms import widgets
from wtforms.compat import string_types

from flask_wtf.file import FileField

from flask_babel import _
from flask_babel import lazy_gettext as _l


class FarmerForm(FlaskForm):
    farmerlocation = StringField(_l("Where do you need help ?"), render_kw={"placeholder": _l("Neuchâtel, Aigle...")}, validators=[InputRequired(message=_l("Bitte füllen Sie dieses Feld aus"))])
    help = StringField(_l("What help do you need ?"), render_kw={"placeholder": _l("Harvesting, Planting...")}, validators=[InputRequired(message=_l("Bitte füllen Sie dieses Feld aus"))])
    details = StringField(_l("Additional details"), render_kw={"placeholder": _l("Good shape, Boots...")}, validators=[InputRequired(message=_l("Bitte füllen Sie dieses Feld aus"))])
    when = StringField(_l("When?"), render_kw={"placeholder": _l("Every Sunday morning")}, validators=[InputRequired(message=_l("Bitte füllen Sie dieses Feld aus"))])
    phone = StringField(_l("Phone number"), render_kw={"placeholder": _l(" ")}, validators=[InputRequired(message=_l("Bitte füllen Sie dieses Feld aus"))])
    email = EmailField(_l("E-Mail:"),  render_kw={"placeholder": _l(" ")}, validators=[InputRequired(message=_l("Bitte füllen Sie dieses Feld aus")), Email(message=_l("Bitte geben Sie eine gültige E-Mailadresse an"))])
    exchange = StringField(_l("What can you offer in exchange?"), render_kw={"placeholder": _l("Fresh produce, travel stipend…")}, validators=[InputRequired(message=_l("Bitte füllen Sie dieses Feld aus"))])
    photo = FileField(_l("Photo of the farm"))

    # hidden fields: used to get data from places API and store it in db
    formatted_address = HiddenField()
    lat = HiddenField()
    lng = HiddenField()

    farmerSubmit = SubmitField(_l("Submit"))



class HelperForm(FlaskForm):
    helperlocation = StringField(_l("Where do you live ?"), render_kw={"placeholder": _l("Start typing...")}, validators=[InputRequired()])

    helperSubmit = SubmitField(_l("Submit"))


class VerficationForm(FlaskForm):
    verificationCode = StringField(_l("Please enter the verification code we sent to your E-Mail address."))
    submit = SubmitField(_l("Verify!"))


class FarmDeletionVerificationForm(FlaskForm):
    verificationCode = StringField(_l("Please enter the verification code we sent to your E-Mail address"))
    submit = SubmitField(_l("Delete Farm!"))

class LoginForm(FlaskForm):
    username = StringField(_("Username"))
    password = PasswordField(_("Password"))

    submit = SubmitField(_l("Login!"))
