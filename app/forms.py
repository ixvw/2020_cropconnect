from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, HiddenField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Optional, InputRequired, Email, StopValidation
from wtforms import widgets
from wtforms.compat import string_types

from flask_wtf.file import FileField

from flask_babel import _
from flask_babel import lazy_gettext as _l


class FarmerForm(FlaskForm):
    farmerlocation = StringField(_l("Where is your farm?"), render_kw={"placeholder": _l("start typing...")}, validators=[InputRequired()])
    help = StringField(_l("Help needed?"), validators=[InputRequired()])
    details = StringField(_l("Additional details"), validators=[InputRequired()])
    when = StringField(_l("When?"), validators=[InputRequired()])
    phone = StringField(_l("Phone number"), validators=[InputRequired()])
    email = EmailField(_l("E-Mail:"), validators=[InputRequired()])
    exchange = StringField(_("in exchange for"), validators=[InputRequired()])
    photo = FileField(_("Photo"))

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

class FarmDeletionVerificationForm(FlaskForm):
    verificationCode = StringField(_l("Please enter the verification code we sent to your E-Mail address"))
    submit = SubmitField(_l("Delete Farm!"))

