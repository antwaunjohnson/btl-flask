# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

from os import environ


class Config(object):
    SECRET_KEY = environ.get("SECRET_KEY")
    SECURITY_PASSWORD_SALT = environ.get("SECURITY_PASSWORD_SALT")
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = True
    SECURITY_RECOVERABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_POST_LOGIN_VIEW = "/user-info"
    SECURITY_POST_REGISTER_VIEW = "/user-info"
    MAIL_SERVER = environ.get("MAIL_SERVER")
    MAIL_USERNAME = environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = environ.get("MAIL_DEFAULT_SENDER")
    MAIL_PORT = environ.get("MAIL_PORT")
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True



class Development(Config):
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False