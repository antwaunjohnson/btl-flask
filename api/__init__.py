from flask import Flask

from .extensions import db, ma, security, babel
from .config import Development
from .commands import create_db, shell_context_processor, drop_db
from .commands import create_roles
from .Models.user_model import user_datastore


def create_app():
    app = Flask(__name__)

    app.config.from_object(Development)

    db.init_app(app)
    ma.init_app(app)
    security.init_app(app, user_datastore)
    babel.init_app(app)
    
    
    app.cli.add_command(create_db)  
    app.cli.add_command(drop_db)
    app.cli.add_command(create_roles)  
    app.shell_context_processors.append(shell_context_processor)  

    from api.Routes.admin_routes import admin
    app.register_blueprint(admin)
    

    return app