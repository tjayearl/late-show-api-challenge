from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from server.models.user import User
from server.extensions import db, jwt
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data.get('username') or not data.get('password'):
        return jsonify(message="Username and password are required."), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify(message="User already exists."), 409

    hashed_pw = generate_password_hash(data['password'])
    new_user = User(username=data['username'], password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message="User registered successfully."), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200

    return jsonify(message="Invalid credentials."), 401