from flask import Flask
from dotenv import load_dotenv
from db import create_tables
from blueprints.user_blueprint import user_bp
from blueprints.post_blueprint import post_bp
load_dotenv()

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(post_bp)

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
