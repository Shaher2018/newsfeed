from flask import jsonify
import re
from models import User

def validate_post_data(data):
    if not data.get('content'):
        return jsonify({"error": "content is required"}), 400
    if not isinstance(data['content'], str) or len(data['content'].strip()) == 0:
        return jsonify({"error": "content must be a non-empty string"}), 400
    return None


def validate_user_data(data):
    if not data.get('username'):
        return jsonify({"error": "username is required"}), 400
    if len(data['username']) < 3 or len(data['username']) > 50:
        return jsonify({"error": "username must be between 3 and 50 characters"}), 400

    if not data.get('email'):
        return jsonify({"error": "email is required"}), 400
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, data['email']):
        return jsonify({"error": "Invalid email format"}), 400

    if not data.get('password'):
        return jsonify({"error": "password is required"}), 400
    if len(data['password']) < 6:
        return jsonify({"error": "password must be at least 6 characters long"}), 400
    
    check_user_email = User.get_user_by_email(data['email'])
    if check_user_email:
        return jsonify({"error": "Email already exists"}), 400
    
    check_user_username = User.get_user_by_username(data['username'])
    if check_user_username:
        return jsonify({"error": "Username already exists"}), 400
    return None

def validate_login_data(data):
    if not data.get('username'):
        return jsonify({"error": "username is required"}), 400
    if not isinstance(data['username'], str) or len(data['username'].strip()) == 0:
        return jsonify({"error": "username must be a non-empty string"}), 400

    if not data.get('password'):
        return jsonify({"error": "password is required"}), 400
    if not isinstance(data['password'], str) or len(data['password'].strip()) == 0:
        return jsonify({"error": "password must be a non-empty string"}), 400
    
    return None


