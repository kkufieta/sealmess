from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from ..database import setup_db, db_drop_and_create_all, Customer, Provider, MenuItem

app = Flask(__name__)
setup_db(app)

# Do this only when you want to delete & reset the entire DB!
# db_drop_and_create_all()

@app.route('/')
def home():
    customer = Customer(first_name="kat", last_name="Kufieta", address="home", phone="347")
    customer.insert()
    print(customer)

    provider = Provider(name="Pizza Heat", address="around the corner", phone="2345", description="Best pizza in town")
    provider.insert()
    print(provider)

    menu_item = MenuItem(provider_id=1, name="margarita", description="cheesy pizza",
                         price=10.00, image_link="https://media.giphy.com/media/4ayiIWaq2VULC/giphy.gif")
    menu_item.insert()
    print(menu_item)

    return 'Hello, kat!'