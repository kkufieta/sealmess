from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, kat!'