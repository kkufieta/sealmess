from flask import request
from ..database import setup_db, db_drop_and_create_all, Customer, Provider, MenuItem, Order
from .shared import app
from .errors import *

# Do this only when you want to delete & reset the entire DB!
# db_drop_and_create_all()
@app.route('/')
def home():
    return jsonify({
        'success': True,
        'message': "Welcome to Sealmess!"
    })


'''
Can be used to populate the database with data, e.g. for testing.
'''
@app.route('/createdata')
def create_data():
    # Create providers
    providers = [
        {'name': 'Sushi',
         'address': 'Sushi Heaven',
         'phone': 'sss-sss-ssss',
         'description': 'Fishy!',
         'image_link': 'https://gph.is/2hKe26d'},
        {'name': 'Korean BBQ',
         'address': 'Korea Town',
         'phone': 'kkk-kkk-kkkk',
         'description': 'Best food in the world',
         'image_link': 'https://media.giphy.com/media/ZQOEnmxm7vmvK/giphy.gif'},
        {'name': 'Deutsche Kueche',
         'address': 'Little Germany',
         'phone': 'ddd-ddd-dddd',
         'description': 'Sauerkraut und Bratwurst',
         'image_link': 'https://media.giphy.com/media/dZC1zOwX203KfwfM6Z/giphy.gif'},
        {'name': 'Italian',
         'address': 'Sicily',
         'phone': 'iii-iii-iiii',
         'description': 'Delicious!',
         'image_link': 'https://media.giphy.com/media/oS2lkrdaq3a3m/giphy.gif'}
    ]
    for p in providers:
        provider = Provider(name=p['name'], address=p['address'],
                            phone=p['phone'], description=p['description'],
                            image_link=p['image_link'])
        provider.insert()

    # Create menu items
    menu_items = [
        {'provider_id': 1,
         'name': 'Salmon Avocado Roll',
         'description': 'Salmon',
         'price': 5.99,
         'image_link': 'https://media.giphy.com/media/3og0IJD4VvwWc7ZepO/giphy.gif'},
        {'provider_id': 1,
         'name': 'Tuna Avocado Roll',
         'description': 'Tuna',
         'price': 4.99,
         'image_link': 'https://media.giphy.com/media/SuxKy4GcbDbBkl0ypo/giphy.gif'},
        {'provider_id': 2,
         'name': 'Hang-ali Yangnyeom Sogalbi',
         'description': 'Short rib marinated',
         'price': 41.95,
         'image_link': 'https://media.giphy.com/media/XynKEMX8oJo9IL5VOd/giphy.gif'},
        {'provider_id': 2,
         'name': 'Dak Gui',
         'description': 'Chicken',
         'price': 32.95,
         'image_link': 'https://media.giphy.com/media/eynU9e3p7uS08/giphy.gif'},
        {'provider_id': 3,
         'name': 'Spaetzle',
         'description': 'German pasta',
         'price': 10.01,
         'image_link': 'https://media.giphy.com/media/LS9AVZdn3d9XFJXTO0/giphy.gif'},
        {'provider_id': 3,
         'name': 'Maultaschen',
         'description': 'German pierogi',
         'price': 15.15,
         'image_link': 'https://media.giphy.com/media/8L195VilfI3cEj8I0t/giphy.gif'},
        {'provider_id': 4,
         'name': 'Pasta Carbonara',
         'description': 'Simply good',
         'price': 12.00,
         'image_link': 'https://media.giphy.com/media/2AbjsquX2K9JC/giphy.gif'},
        {'provider_id': 4,
         'name': 'Lasagne',
         'description': 'Layers',
         'price': 15.00,
         'image_link': 'https://media.giphy.com/media/iDIQmTZitjRZCLkq2o/giphy.gif'}
    ]
    for m in menu_items:
        menu_item = MenuItem(provider_id=m['provider_id'], name=m['name'],
                             description=m['description'], price=m['price'],
                             image_link=m['image_link'])
        menu_item.insert()

    # Create customers
    customers = [
        {'first_name': 'Kat',
         'last_name': 'K.',
         'address': 'home',
         'phone': 'kkk-kkk-kkkk'},
        {'first_name': 'Bboy',
         'last_name': 'B.',
         'address': 'bboys home',
         'phone': 'bbb-bbb-bbbb'}
    ]
    for c in customers:
        customer = Customer(
            first_name=c['first_name'],
            last_name=c['last_name'],
            address=c['address'],
            phone=c['phone'])
        customer.insert()

    # Create orders
    orders = [
        {'customer_id': 1,
         'status': 'eaten',
         'menu_items': [1, 2, 4]},
        {'customer_id': 1,
         'status': 'in process',
         'menu_items': [7]},
        {'customer_id': 2,
         'status': 'eaten',
         'menu_items': [6, 3, 8]},
        {'customer_id': 2,
         'status': 'in process',
         'menu_items': [5, 6]},
        {'customer_id': 2,
         'status': 'delivered',
         'menu_items': [2, 3]}
    ]
    for o in orders:
        menu_items = []
        for menu_item_id in o['menu_items']:
            menu_item = MenuItem.query.filter(
                MenuItem.id == menu_item_id).one_or_none()
            if not menu_item:
                abort(400)
            menu_items.append(menu_item)
        order = Order(customer_id=o['customer_id'], status=o['status'],
                      menu_items=menu_items)
        order.insert()
    return jsonify({
        'success': True,
        'message': 'Successfully created data. You can dump it now into a *.psql file using this command: `pg_dump dbname > outfile`.'
    })
