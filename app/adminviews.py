from flask_admin.contrib.sqla import ModelView
from app.database import Farm
from app import db

from app import admin

admin.add_view(ModelView(Farm, db.session))


