from flask import jsonify
from app import app, app_log

__author__ = 'Xiaoxiao.Xiong'


class CustomError(Exception):

    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)

        self.message = message

        if status_code is not None:
            self.status_code = status_code

        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status_code'] = self.status_code
        return rv


class NotAuthorized(CustomError):
    def __init__(self, message="Not Authorized", payload=None):
        CustomError.__init__(self, message, 401, payload)


class PermissionDenied(CustomError):
    def __init__(self, message="Permission Denied", payload=None):
        CustomError.__init__(self, message, 403, payload)

class NotFound(CustomError):
    def __init__(self, message="Not Found", payload=None):
        CustomError.__init__(self, message, 404, payload)

class NotAllowed(CustomError):
    def __init__(self, message="Method Not Allowed", payload=None):
        CustomError.__init__(self, message, 405, payload)


@app.errorhandler(CustomError)
def handle_custom_err(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    app_log.error(repr(response), extra={'sender': 'DataSource'})
    return response


# Generic handlers
@app.errorhandler(NotImplementedError)
def not_implemented(e):
    status_code = 501
    response = jsonify({
        'status': status_code,
        'message': 'Not Implemented Yet'
    })
    response.status_code = status_code
    app_log.error(repr(response), extra={'sender': 'DataSource'})
    return response


@app.errorhandler(BaseException)
def general_err(e):
    status_code = 500
    response = jsonify({
        "status": status_code,
        "message": ("{0}: {1}").format(
            type(e).__name__,
            repr(e))
    })
    response.status_code = status_code
    app_log.error(repr(response), extra={'sender': 'DataSource'})
    return response