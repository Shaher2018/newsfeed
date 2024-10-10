""" This Section handles all the serializations """
from models import User, Post

class BaseSerializer:
    def serialize(self):
        raise NotImplementedError("Subclasses must implement serialize method")

    def deserialize(self, data):
        raise NotImplementedError("Subclasses must implement deserialize method")


class UserSerializer(BaseSerializer):
    def __init__(self, user):
        self.user = user

    def serialize(self):
        return {
            "id": self.user.id,
            "username": self.user.username,
            "email": self.user.email,
            "created_at": self.user.created_at,
        }

    def deserialize(self, data):
        return User(
            username=data.get("username"),
            email=data.get("email"),
            password=data.get("password"),
        )



class PostSerializer(BaseSerializer):
    def __init__(self, post):
        self.post = post

    def serialize(self):
        return {
            "id": self.post[0],
            "content": self.post[2],
            "created_at": self.post[3]
        }

    def deserialize(self, data):
        return Post(
            user_id=data.get("user_id"),
            content=data.get("content")
        )
