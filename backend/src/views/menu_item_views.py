from flask import request
from ..database import setup_db, db_drop_and_create_all, Customer, Provider, MenuItem, Order
from .shared import app
from .errors import *

'''
Routes: MenuItem (RBAC Provider)
    - POST /providers
    - PATCH /providers/<int: provider_id>

RBAC Provider, Owner:
    - DELETE /providers/<int: provider_id>

Public:
    - GET /providers
    - GET /providers/<int: provider_id>
'''

# POST /providers/<provider_id>/menu
#   Add a new menu item to the DB
#   Creates a new row in the menu_items table
#   Requires the 'post:menu' permission
@app.route('/providers/<provider_id>/menu', methods=['POST'])
# @requires_auth('post:menu')
# def post_menu_item(jwt_payload, provider_id):
def post_menu_item(provider_id):
    if not provider_id:
        abort(400)
    body = request.get_json()
    if not body:
        abort(400)
    keys = ['provider_id', 'name', 'description', 'price']
    if not all(key in body for key in keys):
        abort(422)
    if str(body['provider_id']) != str(provider_id):
        abort(422)
    if not isinstance(body['provider_id'], int):
        abort(422)
    if not all(isinstance(body[key], str) for key in
               ['name', 'description']):
        abort(422)
    if not isinstance(body['price'], float):
        abort(422)
    try:
        provider_id = body['provider_id']
        name = body['name']
        description = body['description']
        price = body['price']
        if 'image_link' in body:
            image_link = body['image_link']
        else:
            image_link = ''
        # create menu item
        menu_item = MenuItem(provider_id=provider_id, name=name,
                             description=description, price=price,
                             image_link=image_link)
        menu_item.insert()
        return jsonify({
            'success': True,
            'created_id': menu_item.id,
            'menu_item': menu_item.format()
        })
    except Exception as e:
        abort(400)


# GET /providers -- Get all providers
@app.route('/providers__', methods=['GET'])
def get_providers_():
    # Get all providers, return a list of providers
    # as a json, and success
    return jsonify({
        'success': False
    })

# GET /providers/<int:provider_id>
@app.route('/providers/<int:provider_id>__', methods=['GET'])
def get_provider_(provider_id):
    # Get provider based on id, return provider information
    # as a json, and success
    return jsonify({
        'success': False
    })

# PATCH /providers/<int:provider_id>
@app.route('/providers/<int:provider_id>__', methods=['PATCH'])
# @requires_auth('patch:providers')
# def patch_provider(jwt_payload, provider_id):
def patch_provider_(provider_id):
    # Grab the provider, patch the provider with new data,
    # return success and patched provider data
    return jsonify({
        'success': False
    })

# DELETE /providers/<int:provider_id>
@app.route('/providers/<int:provider_id>__', methods=['DELETE'])
# @requires_auth('delete:providers')
# def delete_provider(jwt_payload, provider_id):
def delete_provider_(provider_id):
    # delete provider, return deleted_id
    return jsonify({
        'success': False
    })