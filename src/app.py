import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient
from routes import pages
import secrets
secret_key = secrets.token_hex(24)


load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["MONGODB_URI"] = os.environ.get("MONGODB_URI")
    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", secret_key
    )
    app.db = MongoClient(app.config["MONGODB_URI"])
    app.db = app.db['movie_watclist']


    app.register_blueprint(pages)
    return app
app = create_app()
app.run(debug=True, port = 5050)