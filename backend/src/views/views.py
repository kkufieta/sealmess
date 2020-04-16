from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from ..database import setup_db, db_drop_and_create_all, Customer, Provider, MenuItem, Order

app = Flask(__name__)
setup_db(app)

# Do this only when you want to delete & reset the entire DB!
# db_drop_and_create_all()

@app.route('/')
def home():
    print("---create customers kat and brian---")
    customer = Customer(first_name="kat", last_name="Kufieta", address="home", phone="347")
    customer.insert()
    print(customer)

    customer = Customer(first_name="brian", last_name="segers", address="his home", phone="679")
    customer.insert()
    print(customer)

    print("---create providers pizza and candy---")
    provider = Provider(name="Pizza Heat", address="around the corner", phone="2345", description="Best pizza in town")
    provider.insert()
    print(provider)

    provider = Provider(name="kats candy store", address="on the floor", phone="2345", description="gives you cavities")
    provider.insert()
    print(provider)

    print("---menu item 1---")
    menu_item_1 = MenuItem(provider_id=1, name="margarita", description="cheesy pizza",
                         price=10.00, image_link="https://media.giphy.com/media/4ayiIWaq2VULC/giphy.gif")
    menu_item_1.insert()
    print(menu_item_1)

    print("---menu item 2---")
    menu_item_2 = MenuItem(provider_id=2, name="candy", description="kat eats nothing but candy",
                         price=1.00, image_link="")
    menu_item_2.insert()
    print(menu_item_2)

    print("--- orders ---")
    order = Order(customer_id=1, status="eaten!")
    order.add_menu_item(menu_item_2) 
    order.insert()
    print(order)

    order = Order(customer_id=2, status="being baked")
    order.add_menu_item(menu_item_1)
    order.insert()
    print(order)

    print("--- customers ---")
    customer = Customer.query.filter(Customer.id == 1).one()
    print(customer)
    customer = Customer.query.filter(Customer.id == 2).one()
    print(customer)

    return 'Hello, kat!'