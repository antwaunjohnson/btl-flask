from flask import Flask

from .extensions import db, ma, security
from .config import Development

def create_app():
    app = Flask(__name__)

    app.config.from_object(Development)

    db.init_app(app)
    ma.init_app(app)
    security.init_app(app)

    from .route import test
    app.register_blueprint(test)

    return app