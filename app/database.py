from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    formatted_address = db.Column(db.String)  # as received from places API
    lat = db.Column(db.FLOAT)  # .geometry.location.lat() from places API
    lng = db.Column(db.FLOAT)  # .geometry.location.lng() from places API

    help = db.Column(db.String)
    details = db.Column(db.String)
    when = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String)
    imgname = db.Column(db.String)

    # verification
    validationId = db.Column(db.String)
    verificationCode = db.Column(db.String)
    verified = db.Column(db.Boolean, default=False)

    # verified deletion
    deletionId = db.Column(db.String)
    deletionCode = db.Column(db.String)

