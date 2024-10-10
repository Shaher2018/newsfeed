from flask import Blueprint, request, jsonify
from models import User
from serializers import UserSerializer
from validations import validate_user_data, validate_login_data
from utils import verify_password, create_jwt

user_bp = Blueprint('user_bp', __name__)

# Create User
@user_bp.route('/user', methods=['POST'])
def create_user():
    try:
        data = request.json
        validation_error = validate_user_data(data)
        if validation_error:
            return validation_error
        user_serializer = UserSerializer(None)
        user = user_serializer.deserialize(data)
        User.create(user)
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        return jsonify({"error": "Can not create this user"}), 500




@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    validation_error = validate_login_data(data)
    if validation_error:
        return validation_error

    username = data['username']
    password = data['password']
    user = User.get_user_by_username(username)
    if not user or not verify_password(password, user.password):
        return jsonify({"error": "Invalid credentials"}), 401
    token = create_jwt(user.id)
    return jsonify({"token": token}), 200




