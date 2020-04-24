from flask import jsonify, abort
from .shared import app
from ..auth import AuthError

# ===============================
# Authentication & Identification
# ===============================
'''
Error handler for AuthError.
'''
@app.errorhandler(AuthError)
def auth_error(error):
    message, status_code = error.args

    return jsonify({
        'success': False,
        'error': status_code,
        'message': message['code'] + ': ' + message['description']
    }), status_code


'''
401 error handler: unauthorized
    Although the HTTP standard specifies "unauthorized",
    semantically this response means "unauthenticated".
    That is, the client must authenticate itself to get the
    requested response.
'''
@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        'success': False,
        'error': 401,
        'message': 'unauthorized'
    }), 401


'''
403 error handler: forbidden
    The client does not have access rights to the content;
    that is, it is unauthorized, so the server is refusing
    to give the requested resource. Unlike 401, the client's
    identity is known to the server.
'''
@app.errorhandler(403)
def forbidden(error):
    return jsonify({
        'success': False,
        'error': 403,
        'message': 'forbidden'
    }), 403


# ==================================
# Other, general HTTP error handlers
# ==================================
'''
400 error handler: bad request
    The server could not understand the request due to invalid syntax.
'''
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'success': False,
        'error': 400,
        'message': 'bad request'
    }), 400


'''
404 error handler: not found
    The server can not find the requested resource.
    In the browser, this means the URL is not recognized.
    In an API, this can also mean that the endpoint is valid
    but the resource itself does not exist. Servers may also
    send this response instead of 403 to hide the existence
    of a resource from an unauthorized client.
'''
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'resource not found'
    }), 404


'''
405 error handler: Method not allowed
    The request method is known by the server but has been
    disabled and cannot be used. For example, an API may
    forbid DELETE-ing a resource. The two mandatory methods,
    GET and HEAD, must never be disabled and should not
    return this error code.
'''
@app.errorhandler(405)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 405,
        'message': 'method not allowed'
    }), 405


'''
422 error handler: unprocessable entity
    The request was well-formed but was unable to be followed
    due to semantic errors.
'''
@app.errorhandler(422)
def unprocessable_entity(error):
    return jsonify({
        'success': False,
        'error': 422,
        'message': 'unprocessable entity'
    }), 422


'''
500 error handler: internal server error
    The server has encountered a situation it doesn't
    know how to handle.
'''
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': 'internal server error'
    }), 500
