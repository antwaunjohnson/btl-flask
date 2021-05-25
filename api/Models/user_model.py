from flask_security import UserMixin, RoleMixin, SQLAlchemyUserDatastore
from sqlalchemy.orm import backref
from api.extensions import db

from datetime import datetime


class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    last_login_at = db.Column(db.DateTime, default=datetime.utcnow)
    current_login_at = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    roles = db.relationship('Role', secondary='roles_users', backref=backref('users', lazy='dynamic'))

    def get_users():
        """Return list of all users"""
        attrs = (
            "email",
            "active",
            "confirmed_at",
            "create_datetime",
            "update_datetime",
            "last_login_at"
        )
        query = User.user_model.query
        users = query.all()

        info = []
        for user in users:
            userdata = {}
            for attr in attrs:
                userdata[attr] = getattr(user, attr)
                userdata['roles'] = [r.name for r in user.roles]
                info.append(userdata)

                return {"msg" : [], "data": info}

    


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
