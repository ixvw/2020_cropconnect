import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "SjwqLxBN5C_WJp3h0pDjWF42YrZF5C1R"
