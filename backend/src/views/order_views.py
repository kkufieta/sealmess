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
# POST /customers/<int: customer_id>/order
#   Add a new order to the customer with <customer_id>
#   Creates a new row in the orders table
#   Requires the 'post:order' permission
@app.route('/customers/<int:customer_id>/orders', methods=['POST'])
# @requires_auth('post:order')
# def post_order(jwt_payload, customer_id):
def post_order(customer_id):
    if not customer_id:
        abort(400)
    body = request.get_json()
    if not body:
        abort(400)
    keys = ['customer_id', 'status', 'menu_item_ids']
    if not all(key in body for key in keys):
        abort(422)
    try:
        customer_id = body['customer_id']
        status = body['status']
        menu_item_ids = body['menu_item_ids']
        menu_items = []
        for menu_item_id in menu_item_ids:
            menu_item = MenuItem.query.filter(MenuItem.id == menu_item_id).one_or_none()
            if not menu_item:
                abort(422)
            menu_items.append(menu_item)
        order = Order(customer_id=customer_id, status=status, menu_items=menu_items)
        order.insert()

        return jsonify({
            'success': True,
            'created_id': order.id,
            'order': order.format()
        })
    except Exception as e:
        abort(400)

# order = Order(customer_id=customer_id, menu_item_id=menu_item_id)
# order.insert()
# order = Order.query.filter(Order.id == order_id).one_or_none()
# menu_item = MenuItem.query.filter(MenuItem.id == menu_item_id).one_or_none()
# if order and menu_item:
    # order.add_menu_item(menu_item)
    # order.update()

# GET /customers/<int: customer_id>/order - Get the order of a customer
@app.route('/customers/<int:customer_id>/orders', methods=['GET'])
# @requires_auth('post:providers-menu')
# def delete_provider(jwt_payload, provider_id):
def get_order(customer_id):
    # post menu item to menu of the provider given by provider_id
    return jsonify({
        'success': False
    })

# GET /customers/<int: customer_id>/order/<int: order_item_id> - Get an order item
@app.route('/customers/<int:customer_id>/orders/<int:order_id>', methods=['GET'])
# @requires_auth('post:providers-menu')
# def delete_provider(jwt_payload, provider_id):
def get_order_item(customer_id):
    # post menu item to menu of the provider given by provider_id
    return jsonify({
        'success': False
    })

# PATCH /customers/<int: customer_id>/order/<int: order_item_id>
@app.route('/customers/<int:customer_id>/orders/<int:order_id>', methods=['PATCH'])
# @requires_auth('post:providers-menu')
# def delete_provider(jwt_payload, provider_id):
def patch_order_item(customer_id, order_item_id):
    # post menu item to menu of the provider given by provider_id
    return jsonify({
        'success': False
    })

# DELETE /customers/<int: customer_id>/order/<int: order_item_id>
@app.route('/customers/<int:customer_id>/orders/<int:order_item_id>', methods=['DELETE'])
# @requires_auth('post:providers-menu')
# def delete_provider(jwt_payload, provider_id):
def delete_order_item(customer_id, order_item_id):
    # post menu item to menu of the provider given by provider_id
    return jsonify({
        'success': False
    })