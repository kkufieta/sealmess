from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from ..database import setup_db, db_drop_and_create_all, Customer, Provider

app = Flask(__name__)
setup_db(app)

# Do this only when you want to delete & reset the entire DB!
# db_drop_and_create_all()

@app.route('/')
def home():
    customer = Customer(first_name="kat", last_name="Kufieta", address="home", phone="347")
    customer.insert()

    provider = Provider(name="Pizza Heat", address="around the corner", phone="2345", description="Best pizza in town")
    provider.insert()

    return 'Hello, kat!'