from db import get_db_connection
from utils import hash_password

class User:
    def __init__(self, id=None, username=None, email=None, password=None, created_at=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at  # Optional field


    @staticmethod
    def create(user):
        connection = get_db_connection()
        cursor = connection.cursor()
        hashed_password = hash_password(user.password)
        cursor.execute(
            "INSERT INTO User (username, email, password) VALUES (%s, %s, %s)", 
            (user.username, user.email, hashed_password)
        )

        connection.commit()
        cursor.close()

    @staticmethod
    def get_user(user_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM User WHERE id = %s", (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        if user_data:
            return User(**user_data)  # Create User instance
        return None

    @staticmethod
    def get_user_by_username(username):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)  # Fetch results as dictionary

        query = "SELECT * FROM User WHERE username = %s"
        cursor.execute(query, (username,))
        user_data = cursor.fetchone()
        cursor.close()

        if user_data:
            return User(**user_data)
        return None
    @staticmethod
    def get_user_by_email(email):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)  # Fetch results as dictionary

        query = "SELECT * FROM User WHERE email = %s"
        cursor.execute(query, (email,))
        user_data = cursor.fetchone()
        cursor.close()

        if user_data:
            return User(**user_data)
        return None


class Post:
    def __init__(self, user_id, content, post_id=None):
        self.user_id = user_id
        self.content = content
        self.id = post_id  # Optional post_id, will be set after creation if not provided

    @staticmethod
    def create(post):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Post (user_id, content) VALUES (%s, %s)", 
            (post.user_id, post.content)
        )
        post_id = cursor.lastrowid  # Fetch the ID of the inserted post
        connection.commit()
        cursor.close()
        post.id = post_id  # Set the post ID on the object

    @staticmethod
    def get_post(post_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Post WHERE id = %s", (post_id,))
        post = cursor.fetchone()
        cursor.close()
        return post

    @staticmethod
    def update(post_id, content):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE Post SET content = %s WHERE id = %s", (content, post_id))
        connection.commit()
        cursor.execute("SELECT * FROM Post WHERE id = %s", (post_id,))
        post = cursor.fetchone()
        cursor.close()
        return post
    
    @staticmethod
    def delete(post_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Post WHERE id = %s", (post_id,))
        connection.commit()
        cursor.close()

    def to_json(self):
        return {
            "id": self.id,
            "content": self.content
        }


