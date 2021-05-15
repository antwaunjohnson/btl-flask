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


@click.command(name="create_roles")
@with_appcontext
def create_roles():
    """Creates user roles"""
    admin = Role(name='admin', description="The admin has permission to block users, unblock users, ban users, lift bans, edit roles, delete user blogs, create blogs, read blogs, write blogs")
    creator = Role(name='creator', description="The creator has permission to create own blog, delete own blog, edit own blog")

    db.session.add_all([admin, creator])
    db.session.commit()
    


def shell_context_processor():
    return{"db": db, "User": User, "Role": Role, "RolesUsers": RolesUsers}
