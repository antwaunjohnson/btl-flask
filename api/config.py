# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

from os import environ


class Config(object):
    SECRET_KEY = environ.get("SECRET_KEY")
    SECURITY_PASSWORD_SALT = environ.get("SECURITY_PASSWORD_SALT")


class Development(Config):
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False