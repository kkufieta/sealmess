from flask import request
from ..database import setup_db, db_drop_and_create_all, Customer, Provider, MenuItem, Order
from .shared import app
from .errors import *
from ..auth import *

'''
Routes: Customer (RBAC: Customer)
    - POST /customers
    - GET /customers/<int: customer_id>
    - PATCH /customers/<int: customer_id>
    - DELETE /customers/<int: customer_id>
'''
# POST /customers
#   Add a new customer to the DB
#   Creates a new row in the customers table
#   Requires the 'post:customer' permission
@app.route('/customers', methods=['POST'])
@requires_auth('post:customer')
def post_customer(jwt_payload):
    body = request.get_json()
    if not body:
        abort(400)
    keys = ['first_name', 'last_name', 'address', 'phone']
    if not all(key in body for key in keys):
        abort(422)
    if not all(isinstance(body[key], str) for key in keys):
        abort(422)
    try:
        first_name = body['first_name']
        last_name = body['last_name']
        address = body['address']
        phone = body['phone']
        # create customer, return success, customer, and created_id
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            address=address,
                            phone=phone)
        customer.insert()
        # Return created customer
        return jsonify({
            'success': True,
            'created_id': customer.id,
            'customer': customer.format()
        })
    except Exception as e:
        abort(400)

# GET /customers/<int:customer_id>
#   requres the 'get:customer' permission
@app.route('/customers/<int:customer_id>', methods=['GET'])
@requires_auth('get:customer')
def get_customer(jwt_payload, customer_id):
    # Get customer based on id, return customer information
    if not customer_id:
        abort(400)
    customer = Customer.query.filter(Customer.id == customer_id).one_or_none()
    if not customer:
        abort(404)
    return jsonify({
        'success': True,
        'customer': customer.format()
    })

# PATCH /customers/<int:customer_id>
#   responds with 404 if <customer_id> is not found
#   updates the corresponding row for <customer_id>
#   requires the 'patch:customer' permission
@app.route('/customers/<int:customer_id>', methods=['PATCH'])
@requires_auth('patch:customer')
def patch_customer(jwt_payload, customer_id):
    if not customer_id:
        abort(400)
    body = request.get_json()
    if not body:
        abort(400)
    keys = ['first_name', 'last_name', 'address', 'phone']
    if not any(key in body for key in keys):
        abort(400)
    customer = Customer.query.filter(Customer.id == customer_id).one_or_none()
    if not customer:
        abort(404)
    try:
        for key in keys:
            if key in body:
                setattr(customer, key, body[key])
        customer.update()

        return jsonify({
            'success': True,
            'updated_id': customer_id,
            'customer': customer.format()
        })
    except Exception as e:
        abort(400)

# DELETE /customers/<int:customer_id>
#   responds with 404 error if <customer_id> is not found
#   deletes corresponding row for <customer_id>
#   requires the 'delete:customer' permission
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
@requires_auth('delete:customer')
def delete_customer(jwt_payload, customer_id):
    # delete customer, return deleted_id
    if not customer_id:
        abort(400)
    customer = Customer.query.filter(Customer.id == customer_id).one_or_none()
    if not customer:
        abort(404)
    try:
        customer.delete()
        return jsonify({
            'success': True,
            'deleted_id': customer_id
        })
    except Exception as e:
        abort(400)
