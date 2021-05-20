from flask import Blueprint, jsonify, request
from api.extensions import db, ma
from flask_security import current_user, login_required, roles_required
from api.Models.user_model import user_datastore, Role, User


admin = Blueprint('admin', __name__)

class RoleSchema(ma.Schema):
    class Meta:
        fields = ('name', 'description')

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('email', 'active','last_login_at')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@admin.route('/admin/new_admin', methods=['GET','POST'])
@login_required
@roles_required('admin')
def new_admin():
    new_admin = user_datastore.find_or_create_role('admin')
    user_datastore.add_role_to_user(current_user, new_admin)
    db.session.commit()
    return '<h1>You are the admin!</h1>'


@admin.route('/admin/users', methods=['GET'])
@login_required
@roles_required('admin')
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)





    

    
    




# @admin.route('login/edit_role/<id>', methods=['PUT'])
# @login_required
# @roles_required('admin')
# def edit_role(user, role):
#     new_role = user_datastore.remove_role_from_user(user, role)
#     return user_datastore.

#     # role.name = name
#     # db.session.commit()
#     # return user_schema.jsonify(user)
