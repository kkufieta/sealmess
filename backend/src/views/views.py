from flask_sqlalchemy import SQLAlchemy
from ..database import setup_db, db_drop_and_create_all, Customer, Provider, MenuItem, Order
from .shared import app
from .errors import *

setup_db(app)

# Do this only when you want to delete & reset the entire DB!
# db_drop_and_create_all()

@app.route('/')
def home():
    return jsonify({
        'success': True
    })


'''
Routes: Customer (RBAC: Customer)
    - POST /customers
    - GET /customers/<int: customer_id>
    - PATCH /customers/<int: customer_id>
    - DELETE /customers/<int: customer_id>
'''
# POST /customers -- Add a new customer to the DB
@app.route('/customers', methods=['POST'])
# @requires_auth('post:customers')
# def post_customers(jwt_payload):
def post_customers():
    # create customer, return success and created_id
    # Return created customer
    return jsonify({
        'success': False
    })

# GET /customers/<int:customer_id>
@app.route('/customers/<int:customer_id>', methods=['GET'])
# @requires_auth('get:customer')
# def get_customer(jwt_payload, customer_id):
def get_customer(customer_id):
    # Get customer based on id, return customer information
    # as a json, and success
    return jsonify({
        'success': False
    })

# PATCH /customers/<int:customer_id>
@app.route('/customers/<int:customer_id>', methods=['PATCH'])
def patch_customer(customer_id):
    # Grab the customer, patch the customer with new data,
    # return success and patched customer data
    return jsonify({
        'success': False
    })

# DELETE /customers/<int:customer_id>
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
# @requires_auth('delete:customers')
# def delete_customer(jwt_payload, customer_id):
def delete_customer(customer_id):
    # delete customer, return deleted_id
    return jsonify({
        'success': False
    })

'''
Routes: Provider (RBAC Provider)
    - POST /providers
    - PATCH /providers/<int: provider_id>
    - POST /providers/<int: provider_id>/menu
    - PATCH /providers/<int: provider_id>/menu/<int: menu_item_id>

RBAC Provider, Owner:
    - DELETE /providers/<int: provider_id>

RBAC Provider, Customer, Owner:
    - DELETE /providers/<int: provider_id>/menu/<int: menu_item_id>

Public:
    - GET /providers
    - GET /providers/<int: provider_id>
    - GET /providers/<int: provider_id>/menu
    - GET /providers/<int: provider_id>/menu/<int: menu_item_id>
'''
# POST /providers -- Add a new provider to the DB
@app.route('/providers', methods=['POST'])
# @requires_auth('post:providers')
def post_providers():
    # create provider, return success and created_id
    return jsonify({
        'success': False
    })

# GET /providers
@app.route('/providers', methods=['GET'])
def get_provider(provider_id):
    # Get all providers, return a list of providers
    # as a json, and success
    return jsonify({
        'success': False
    })

# GET /providers/<int:provider_id>
@app.route('/providers/<int:provider_id>', methods=['GET'])
def get_provider(provider_id):
    # Get provider based on id, return provider information
    # as a json, and success
    return jsonify({
        'success': False
    })

# PATCH /providers/<int:provider_id>
@app.route('/providers/<int:provider_id>', methods=['PATCH'])
# @requires_auth('patch:providers')
# def patch_provider(jwt_payload, provider_id):
def patch_provider(provider_id):
    # Grab the provider, patch the provider with new data,
    # return success and patched provider data
    return jsonify({
        'success': False
    })

# DELETE /providers/<int:provider_id>
@app.route('/providers/<int:provider_id>', methods=['DELETE'])
# @requires_auth('delete:providers')
# def delete_provider(jwt_payload, provider_id):
def delete_provider(provider_id):
    # delete provider, return deleted_id
    return jsonify({
        'success': False
    })

# GET /providers
# GET /providers/<int: provider_id>
# PATCH /providers/<int: provider_id>
# DELETE /providers/<int: provider_id>

# POST /providers/<int: provider_id>/menu
# PATCH /providers/<int: provider_id>/menu/<int: menu_item_id>
# GET /providers/<int: provider_id>/menu
# GET /providers/<int: provider_id>/menu/<int: menu_item_id>
# DELETE /providers/<int: provider_id>/menu/<int: menu_item_id>


# ======
# ROUTES
# ======
    '''
    customer = Customer(first_name="kat",
                        last_name="Kufieta",
                        address="home",
                        phone="347")
    customer.insert()

    provider = Provider(name="Pizza Heat", address="around the corner", phone="2345", description="Best pizza in town")
    provider.insert()

    provider = Provider(name="kats candy store", address="on the floor", phone="2345", description="gives you cavities")
    provider.insert()

    menu_item_1 = MenuItem(provider_id=1, name="margarita", description="cheesy pizza",
                        price=10.00, image_link=)
    menu_item_1.insert()

    order = Order(customer_id=1, status="eaten!")
    order.add_menu_item(menu_item_2) 
    order.insert()

    customer = Customer.query.filter(Customer.id == 1).one()
    customer = Customer.query.filter(Customer.id == 2).one()
    '''
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