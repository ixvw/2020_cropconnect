from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmerlocation = db.Column(db.String)
    help = db.Column(db.String)
    details = db.Column(db.String)
    when = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String)

    # verification
    validationId = db.Column(db.String)
    verificationCode = db.Column(db.String)
    verified = db.Column(db.Boolean, default=False)

