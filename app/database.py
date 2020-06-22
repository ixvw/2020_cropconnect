from app import app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


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


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)