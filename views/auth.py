import json
import jsonify
from flask import Blueprint, request, session
from errors import *
from model.user import User
from utils import json_response

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/login', methods=['POST'])
def login():
    body_data = request.get_json()
    username = body_data['username']
    password = body_data['password']
    user = User.query.filter_by(username = username).first()
    if not user or user.password != password:
        raise LoginError("Login failed")
    session['username'] = username
    data = {"token": session[username]}
    return json_response(data, 200)


@admin.route('/sddad', methods=['GET'])
def sddad():
    username = session.get('username')
    print(username)
    data = {}
    return json_response(data, 200)