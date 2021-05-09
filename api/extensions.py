from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_security import Security, SQLAlchemyUserDatastore

db = SQLAlchemy()
ma = Marshmallow()

user_datastore = SQLAlchemyUserDatastore
security = Security()