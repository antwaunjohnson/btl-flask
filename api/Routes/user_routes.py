from flask import Blueprint, json, jsonify
from flask_security.core import UserMixin
from flask_security.decorators import roles_required
from api.extensions import db, ma

from flask_security import current_user, login_required
from api.Models.user_model import user_datastore, Role, User

user = Blueprint('user', __name__)


class RoleSchema(ma.Schema):
    class Meta:
        model = Role 
        fields = ('name', 'description')

        
role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('id','email', 'active','last_login_at', 'current_login_at')

        
        

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user.route('/user-info', methods=['GET'])
@login_required
def new_creator():
    user = current_user
    if UserMixin.has_role(user, 'creator' or 'admin'):
        return user_schema.jsonify(user)
    else:
        creator = user_datastore.find_or_create_role('creator')
        user_datastore.add_role_to_user(current_user, creator)
        db.session.commit()
        return user_schema.jsonify(user)

""" Continue investingating how to delete users"""
@user.route('/delete/<id>')
@login_required
def delete_account(id):
    user_datastore.find_user(User.get_id(id))
    user_datastore.delete_user(user)
    db.session.delete(user)
    db.session.commit()
    return jsonify("You're account has been successfully deleted")
