from flask import request
from ..database import setup_db, db_drop_and_create_all, Customer, Provider, MenuItem, Order
from .shared import app
from .errors import *

'''
Routes: Provider (RBAC Provider)
    - POST /providers
    - PATCH /providers/<int: provider_id>

RBAC Provider, Owner:
    - DELETE /providers/<int: provider_id>

Public:
    - GET /providers
    - GET /providers/<int: provider_id>
'''
# POST /providers
#   Add a new provider to the DB
#   Creates a new row in the providers table
# Requires the 'post:providers' permission
@app.route('/providers', methods=['POST'])
# @requires_auth('post:providers')
# def post_providers(jwt_payload)
def post_providers():
    body = request.get_json()
    if not body:
        abort(400)
    keys = ['name', 'address', 'phone', 'description']
    if not all(key in body for key in keys):
        abort(422)
    if not all(isinstance(key, str) for key in keys):
        abort(422)
    try:
        name = body['name']
        address = body['address']
        phone = body['phone']
        description = body['description']
        if 'image_link' in body:
            image_link = body['image_link']
        else:
            image_link = ''
        # create provider
        provider = Provider(name=name, address=address,
                            phone=phone, description=description,
                            image_link=image_link)
        provider.insert()
        return jsonify({
            'success': True,
            'created_id': provider.id,
            'provider': provider.format()
        })
    except Exception as e:
        abort(400)


# GET /providers -- Get all providers
# Open to public
@app.route('/providers', methods=['GET'])
def get_providers():
    # Get all providers, return a list of providers
    try:
        providers = Provider.query.order_by(Provider.id).all()
        return jsonify({
            'success': True,
            'providers': [provider.format() for provider in providers]
        })
    except Exception as e:
        abort(404)

# GET /providers/<int:provider_id>
# Open to public
@app.route('/providers/<int:provider_id>', methods=['GET'])
def get_provider(provider_id):
    if not provider_id:
        abort(400)
    provider = Provider.query.filter(Provider.id == provider_id).one_or_none()
    if not provider:
        abort(404)
    return jsonify({
        'success': True,
        'provider': provider.format()
    })

# PATCH /providers/<int:provider_id>
#   responds with 404 if <provider_id> is not found
#   updates the corresponding row for <provider_id>
#   requires the 'patch:provider' permission
@app.route('/providers/<int:provider_id>', methods=['PATCH'])
# @requires_auth('patch:provider')
# def patch_provider(jwt_payload, provider_id):
def patch_provider(provider_id):
    if not provider_id:
        abort(400)
    body = request.get_json()
    if not body:
        abort(400)
    keys = ['name', 'address', 'phone', 'description', 'image_link']
    if not any(key in body for key in keys):
        abort(400)
    provider = Provider.query.filter(Provider.id == provider_id).one_or_none()
    if not provider:
        abort(404)
    try:
        for key in keys:
            if key in body:
                setattr(provider, key, body[key])
        provider.update()
        return jsonify({
            'success': True,
            'updated_id': provider_id,
            'provider': provider.format()
        })
    except Exception as e:
        abort(400)

# DELETE /providers/<int:provider_id>
@app.route('/providers/<int:provider_id>', methods=['DELETE'])
# @requires_auth('delete:providers')
# def delete_provider(jwt_payload, provider_id):
def delete_provider(provider_id):
    # delete provider, return deleted_id
    return jsonify({
        'success': False
    })