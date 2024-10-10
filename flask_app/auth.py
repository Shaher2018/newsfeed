import jwt
from flask import request, jsonify, g
from functools import wraps
import os

def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "Token is missing!"}), 401
        
        try:
            payload = jwt.decode(token.split(" ")[1], os.getenv("SECRET_KEY"), algorithms=["HS256"])
            user_id = payload.get('user_id')
            g.user_id = user_id
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return jsonify({"error": "Invalid token!"}), 401
        
        return f(*args, **kwargs)
    return decorated
