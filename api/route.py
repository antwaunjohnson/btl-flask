from flask import Blueprint, jsonify

test = Blueprint('test', __name__)

@test.route('/', methods=['GET'])
def testing_route():
    return '<h1>Home Page</h1>'

@test.route('/protected')
def protected():
    return '<h1>Protected Page</h1>'