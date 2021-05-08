from flask import Blueprint, jsonify

test = Blueprint('test', __name__)

@test.route('/', methods=['GET'])
def testing_route():
    return jsonify("The route was successful")