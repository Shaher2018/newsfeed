import bcrypt
import jwt
import datetime
import os

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password, hashed_password):
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


def create_jwt(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }
    token = jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm='HS256')
    return token

def decode_jwt(token):
    try:
        return jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None
