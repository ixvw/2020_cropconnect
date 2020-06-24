from flask_admin.contrib.sqla import ModelView
from app.database import Farm, User
from app import db

from app import admin

from flask_login import current_user


class FarmView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

class UserView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(FarmView(Farm, db.session))
admin.add_view(UserView(User, db.session))


