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
# POST /customers/<int: customer_id>/orders
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

# POST /orders/<int:order_id>/menu_items
#   Add a new menu-item to an existing order with <order_id>
#   Requires the 'post:order' permission
@app.route('/orders/<int:order_id>/menu_items', methods=['POST'])
# @requires_auth('post:order')
# def add_menu_items_to_order(jwt_payload, order_id):
def add_menu_items_to_order(order_id):
    if not order_id:
        abort(400)
    body = request.get_json()
    if not body or not 'menu_item_ids' in body:
        abort(400)
    order = Order.query.filter(Order.id == order_id).one_or_none()
    if not order:
        abort(404)
    try:
        for menu_item_id in body['menu_item_ids']:
            menu_item = MenuItem.query.filter(MenuItem.id == menu_item_id).one_or_none()
            if not menu_item:
                abort(400)
            order.add_menu_item(menu_item)
        order.update()

        return jsonify({
            'success': True,
            'order_id': order.id,
            'order': order.format()
        })
    except Exception as e:
        abort(400)

# GET /customers/<int:customer_id>/orders
#   Get the orders of a customer
@app.route('/customers/<int:customer_id>/orders', methods=['GET'])
# @requires_auth('get:orders')
# def get_orders(jwt_payload, customer_id):
def get_orders(customer_id):
    if not customer_id:
        abort(400)
    try:
        orders = Order.query.filter(Order.customer_id == customer_id).all()
        if not orders:
            abort(404)
        return jsonify({
            'success': True,
            'customer_id': customer_id,
            'orders': [order.format() for order in orders]
        })
    except Exception as e:
        abort(404)
        

# GET /customers/<int:customer_id>/order/<int:order_item_id>
#   Get an order
@app.route('/customers/<int:customer_id>/orders/<int:order_id>', methods=['GET'])
# @requires_auth('get:orders')
# def get_order(jwt_payload, customer_id, order_id):
def get_order(customer_id, order_id):
    if not customer_id or not order_id:
        abort(400)
    order = Order.query.filter(Order.id == order_id).one_or_none()
    if not order:
        abort(404)
    if not order.customer_id == customer_id:
        abort(400)
    return jsonify({
        'success': True,
        'order': order.format(),
        'customer_id': customer_id,
        'order_id': order_id
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