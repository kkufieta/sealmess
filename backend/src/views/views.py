from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from ..database.models import setup_db, db_drop_and_create_all

app = Flask(__name__)
setup_db(app)
db_drop_and_create_all()

@app.route('/')
def home():
    return 'Hello, kat!'