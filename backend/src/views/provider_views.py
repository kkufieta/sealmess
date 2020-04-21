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
@app.route('/providers', methods=['GET'])
def get_providers():
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