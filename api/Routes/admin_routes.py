from flask import Blueprint, jsonify
from api.extensions import db, ma
from flask_security import current_user, login_required, roles_required
from api.Models.user_model import user_datastore, User


admin = Blueprint('admin', __name__)

class RoleSchema(ma.Schema):
    class Meta:
        fields = ('name', 'description')

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('email', 'active','last_login_at', 'current_login_at')
        roles = ma.Nested(RoleSchema, many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)



@admin.route('/admin/new-admin', methods=['GET','POST'])
@login_required
def new_admin():
    new_admin = user_datastore.find_or_create_role('admin')
    user_datastore.add_role_to_user(current_user, new_admin)
    db.session.commit()
    return user_schema.jsonify(current_user)


@admin.route('/admin/users', methods=['GET'])
@login_required
@roles_required('admin')
def get_users():
    all_users = User.query.all()
    result = users_schema.dumps(all_users)
    return jsonify(result)


# Continue work to allow admin to delete users
"""
@admin.route('/admin/delete-user/<id>', methods=['DELETE'])
@login_required
@roles_required('admin')
def delete_user(user):
    user = user_datastore.find_user(User.id)
    user_datastore.delete_user(user)
    db.session.delete(user)
    db.session.commit()
    return f'<h1>The user {user} has been deleted!</h1>'
"""
