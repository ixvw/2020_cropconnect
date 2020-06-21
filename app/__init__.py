from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_babel import Babel
from flask_admin import Admin

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

from app.database import db
db.create_all()

from app import routes
bootstrap = Bootstrap(app)

admin = Admin(app, name="cropconnect", template_mode="bootstrap3")
from app import adminviews