import mysql.connector
import os

# Establish MySQL connection
def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return connection

# Function to create tables
def create_tables():
    connection = get_db_connection()
    cursor = connection.cursor()

    create_user_table = """
    CREATE TABLE IF NOT EXISTS User (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """


    create_post_table = """
    CREATE TABLE IF NOT EXISTS Post (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES User(id)
    );
    """

    create_comment_table = """
    CREATE TABLE IF NOT EXISTS Comment (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        post_id INT,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES User(id),
        FOREIGN KEY (post_id) REFERENCES Post(id)
    );
    """

    create_like_table = """
    CREATE TABLE IF NOT EXISTS `Like` (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        post_id INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES User(id),
        FOREIGN KEY (post_id) REFERENCES Post(id)
    );
    """

    create_share_table = """
    CREATE TABLE IF NOT EXISTS Share (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        post_id INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES User(id),
        FOREIGN KEY (post_id) REFERENCES Post(id)
    );
    """

    create_friendship_table = """
    CREATE TABLE IF NOT EXISTS Friendship (
        id INT AUTO_INCREMENT PRIMARY KEY,
        follower_id INT,
        followed_id INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (follower_id) REFERENCES User(id),
        FOREIGN KEY (followed_id) REFERENCES User(id)
    );
    """

    # Execute table creation commands
    try:
        cursor.execute(create_user_table)
        cursor.execute(create_post_table)
        cursor.execute(create_comment_table)
        cursor.execute(create_like_table)
        cursor.execute(create_share_table)
        cursor.execute(create_friendship_table)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {str(err)}")
    finally:
        cursor.close()
        connection.close()