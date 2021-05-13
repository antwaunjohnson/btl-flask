import click
from flask.cli import with_appcontext
from .extensions import db
from .Models.user_model import User, Role, RolesUsers



@click.command(name="create_db")
@with_appcontext
def create_db():
    """Creates database"""
    db.create_all()
    db.session.commit()

@click.command(name="drop_db")
@with_appcontext
def drop_db():
    """Cleans database"""
    db.drop_all()


def shell_context_processor():
    return{"db": db, "User": User, "Role": Role, "RolesUsers": RolesUsers}
