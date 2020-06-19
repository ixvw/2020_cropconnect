import os
import credentials

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "SjwqLxBN5C_WJp3h0pDjWF42YrZF5C1R"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db/data.sqlite"
    LANGUAGES = ["en", "it", "fr", "de"]
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
