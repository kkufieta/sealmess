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


# GET /providers/<int:provider_id>/menu
#   Get the menu of a provider
#   Open to public
@app.route('/providers/<int:provider_id>/menu', methods=['GET'])
def get_menu(provider_id):
    if not provider_id:
        abort(400)
    try:
        menu = MenuItem.query.filter(MenuItem.provider_id == provider_id).all()
        return jsonify({
            'success': True,
            'menu': [menu_item.format() for menu_item in menu],
            'provider_id': provider_id
        })
    except Exception as e:
        abort(404)


# GET /providers/<int:provider_id>/menu/<int:menu_item_id>
#   Get a menu item out of the menu of a provider
#   Open to public
@app.route('/providers/<int:provider_id>/menu/<int:menu_item_id>', methods=['GET'])
def get_menu_item(provider_id, menu_item_id):
    if not provider_id or not menu_item_id:
        abort(400)
    menu_item = MenuItem.query.filter(MenuItem.id == menu_item_id).one_or_none()
    if not menu_item:
        abort(404)
    if not menu_item.provider_id == provider_id:
        abort(400)
    return jsonify({
        'success': True,
        'menu_item': menu_item.format(),
        'provider_id': provider_id,
        'menu_item_id': menu_item_id
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