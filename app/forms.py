from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, HiddenField, ValidationError
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Optional, InputRequired, Email, StopValidation
from wtforms import widgets
from wtforms.compat import string_types

from flask_wtf.file import FileField

from flask_babel import _
from flask_babel import lazy_gettext as _l


def validate_phone(form, field):
    print("validate_phone validator called!")
    if len(field.data.replace(" ", "")) not in [len("0799999999"), len("+41799999999")]:
        print("ValidatePhone: phone number does not have required length!")
        if field.data[0] not in ["0", "+"]:
            print("ValidatePhone: phone number does not start with + or 0")
            raise ValidationError(_l("Please enter a valid Swiss Phone number! Format 079 999 99 99 or +41 79 999 99 99"))
    print("ValidatePhone validator found nothing wrong with phone number")


class FarmerForm(FlaskForm):
    farmerlocation = StringField(_l("Where is your farm?"), render_kw={"placeholder": _l("start typing...")}, validators=[InputRequired(message=_l("Bitte füllen Sie dieses Feld aus"))])
    help = StringField(_l("Help needed?"), validators=[InputRequired(message=_l("Bitte füllen Sie dieses Feld aus"))])
    details = StringField(_l("Additional details"), validators=[InputRequired(message=_l("Bitte füllen Sie dieses Feld aus"))])
    when = StringField(_l("When?"), validators=[InputRequired(message=_l("Bitte füllen Sie dieses Feld aus"))])
    phone = StringField(_l("Phone number"), validators=[InputRequired(message=_l("Bitte füllen Sie dieses Feld aus")), validate_phone])
    email = EmailField(_l("E-Mail:"), validators=[InputRequired(message=_l("Bitte füllen Sie dieses Feld aus")), Email(message=_l("Bitte geben Sie eine gültige E-Mailadresse an"))])
    exchange = StringField(_("in exchange for"), validators=[InputRequired(message=_l("Bitte füllen Sie dieses Feld aus"))])
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

