from flask import request
from ..database import setup_db, db_drop_and_create_all, Customer, Provider, MenuItem, Order
from .shared import app
from .errors import *

'''
Routes: Order (RBAC Customer)
    - POST /customers/<int: customer_id>/order
    - GET /customers/<int: customer_id>/order
    - GET /customers/<int: customer_id>/order/<int: order_id>
    - DELETE /customers/<int: customer_id>/order/<int: order_id>
'''

# POST /customers/<int: customer_id>/order - Post an order item to
# the order of a customer
@app.route('/customers/<int:customer_id>/order', methods=['POST'])
# @requires_auth('post:providers-menu')
# def delete_provider(jwt_payload, provider_id):
def post_order(customer_id):
    # post menu item to menu of the provider given by provider_id
    return jsonify({
        'success': False
    })

# GET /customers/<int: customer_id>/order - Get the order of a customer
@app.route('/customers/<int:customer_id>/order', methods=['GET'])
# @requires_auth('post:providers-menu')
# def delete_provider(jwt_payload, provider_id):
def get_order(customer_id):
    # post menu item to menu of the provider given by provider_id
    return jsonify({
        'success': False
    })

# GET /customers/<int: customer_id>/order/<int: order_item_id> - Get an order item
@app.route('/customers/<int:customer_id>/order/<int:order_item_id>', methods=['GET'])
# @requires_auth('post:providers-menu')
# def delete_provider(jwt_payload, provider_id):
def get_order_item(customer_id):
    # post menu item to menu of the provider given by provider_id
    return jsonify({
        'success': False
    })

# PATCH /customers/<int: customer_id>/order/<int: order_item_id>
@app.route('/customers/<int:customer_id>/order/<int:order_item_id>', methods=['PATCH'])
# @requires_auth('post:providers-menu')
# def delete_provider(jwt_payload, provider_id):
def patch_order_item(customer_id, order_item_id):
    # post menu item to menu of the provider given by provider_id
    return jsonify({
        'success': False
    })

# DELETE /customers/<int: customer_id>/order/<int: order_item_id>
@app.route('/customers/<int:customer_id>/order/<int:order_item_id>', methods=['DELETE'])
# @requires_auth('post:providers-menu')
# def delete_provider(jwt_payload, provider_id):
def delete_order_item(customer_id, order_item_id):
    # post menu item to menu of the provider given by provider_id
    return jsonify({
        'success': False
    })