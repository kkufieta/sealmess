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
        customer = Customer(first_name=c['first_name'], last_name=c['last_name'],
                            address=c['address'], phone=c['phone'])
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
            menu_item = MenuItem.query.filter(MenuItem.id == menu_item_id).one_or_none()
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

# '''
# GET /drinks
# it should be a public endpoint
# it should contain only the drink.short() data representation
# returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
# or appropriate status code indicating reason for failure
# '''
# @app.route('/drinks', methods=['GET'])
# def get_drinks():
# drinks = Drink.query.all()
# drinks = [drink.short() for drink in drinks]
# return jsonify({
    # 'success': True,
    # 'drinks': drinks
# })


# '''
# GET /drinks-detail
# it should require the 'get:drinks-detail' permission
# it should contain the drink.long() data representation
# returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
# or appropriate status code indicating reason for failure
# '''
# @app.route('/drinks-detail', methods=['GET'])
# @requires_auth('get:drinks-detail')
# def get_drinks_detail(jwt_payload):
# drinks = Drink.query.all()
# drinks = [drink.long() for drink in drinks]
# return jsonify({
    # 'success': True,
    # 'drinks': drinks
# })


# '''
# POST /drinks
# it should create a new row in the drinks table
# it should require the 'post:drinks' permission
# it should contain the drink.long() data representation
# returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
# or appropriate status code indicating reason for failure
# '''
# @app.route('/drinks', methods=['POST'])
# @requires_auth('post:drinks')
# def post_drink(jwt_payload):
# body = request.get_json()
# if not body:
    # abort(400)
# if not all(key in body for key in ['title', 'recipe']):
    # abort(422)
# title = body['title']
# recipe = body['recipe']
# if not isinstance(recipe, list):
    # abort(422)
# for recipe_part in recipe:
    # if not all(key in recipe_part for key in ['color', 'name', 'parts']):
        # abort(422)
# recipe = json.dumps(recipe)
# try:
    # drink = Drink(title=title, recipe=recipe)
    # drink.insert()
    # return jsonify({
        # 'success': True,
        # 'drinks': drink.long()
    # })
# except Exception:
    # abort(400)


# '''
# PATCH /drinks/<id>
# where <id> is the existing model id
# it should respond with a 404 error if <id> is not found
# it should update the corresponding row for <id>
# it should require the 'patch:drinks' permission
# it should contain the drink.long() data representation
# returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
# or appropriate status code indicating reason for failure
# '''
# @app.route('/drinks/<int:id>', methods=['PATCH'])
# @requires_auth('patch:drinks')
# def patch_drink(jwt_payload, id):
# if not id:
    # abort(404)
# try:
    # drink = Drink.query.filter(Drink.id == id).one_or_none()
    # if not drink:
        # abort(404)
    # body = request.get_json()
    # if not body:
        # abort(400)
    # if not any(key in body for key in ['title', 'recipe']):
        # abort(400)
    # if 'title' in body:
        # drink.title = body['title']
    # if 'recipe' in body:
        # recipe = body['recipe']
        # if not isinstance(recipe, list):
            # abort(422)
        # for recipe_part in recipe:
            # if not all(
                # key in recipe_part for key in [
                    # 'color',
                    # 'name',
                    # 'parts']):
                # abort(422)
        # drink.recipe = json.dumps(body['recipe'])
    # drink.update()
    # return jsonify({
        # 'success': True,
        # 'drinks': [drink.long()]
    # })
# except Exception:
    # abort(404)


# '''
# DELETE /drinks/<id>
# where <id> is the existing model id
# it should respond with a 404 error if <id> is not found
# it should delete the corresponding row for <id>
# it should require the 'delete:drinks' permission
# returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
# or appropriate status code indicating reason for failure
# '''
# @app.route('/drinks/<int:id>', methods=['DELETE'])
# @requires_auth('delete:drinks')
# def delete_drink(jwt_payload, id):
# if not id:
    # abort(404)
# try:
    # drink = Drink.query.filter(Drink.id == id).one_or_none()
    # if not drink:
        # abort(404)
    # drink.update()
    # drink.delete()
    # return jsonify({
        # 'success': True,
        # 'delete': id
    # })
# except Exception:
    # abort(404)