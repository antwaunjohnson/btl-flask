from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_security import Security
from flask_babelex import Babel
from flask_mail import Mail

db = SQLAlchemy()
ma = Marshmallow()
security = Security()
babel = Babel()
mail = Mail()