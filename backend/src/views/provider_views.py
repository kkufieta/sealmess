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
# POST /providers -- Add a new provider to the DB
@app.route('/providers', methods=['POST'])
# @requires_auth('post:providers')
def post_providers():
    # create provider, return success and created_id
    return jsonify({
        'success': False
    })

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