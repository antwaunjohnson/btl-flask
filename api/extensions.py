from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_security import Security

db = SQLAlchemy()
ma = Marshmallow()
security = Security()