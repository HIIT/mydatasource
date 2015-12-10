import jwt
import json
import urllib2
from functools import wraps
from flask import request
from app.handler.dbHelper import DBHelper
from app.config import DOP_API_RPT

from app.handler.error_handler import CustomError, PermissionDenied, NotAuthorized


__author__ = 'Xiaoxiao.Xiong'


def validate_token(auth):
    """
    Inspect ext_id
    :param auth: the content of HTTP Authorization header
    :return: Boolean true/false
    """
    parts = auth.split()

    if len(parts) != 2:
        raise CustomError('Wrong context of Authorization Header')

    if parts[0].lower() != 'bearer':
        raise CustomError('Unsupported authorization type')

    if DBHelper.check_token(parts[1]):
        return True
    else:
        return False


def require_token(fn):
    @wraps(fn)
    def _wrap(*args, **kwargs):

        if 'Authorization' not in request.headers:
            raise CustomError('Authorization header Required')

        auth = request.headers['Authorization']

        f = validate_token(auth)
        if f is not True:
            raise PermissionDenied(payload={'detail': 'Invalid ext_id'})
        return fn(*args, **kwargs)

    return _wrap


def validate_rpt(rpt):
    """
    Inspect RPT via requesting api of DOP
    :param rpt: JWT Token
    :return: Boolean, if RPT valid return True, otherwise return False
    """
    try:

        req = urllib2.Request(DOP_API_RPT, json.dumps({'rpt':rpt}))
        req.add_header('Content-Type', 'application/json')

        f = urllib2.urlopen(req, timeout=4).read()

        obj = json.loads(f)

        if 'status' not in obj:
            raise AttributeError('Authorization server did not response an expecting message')

        if obj['status'] == True:
            return True
        elif obj['status'] == False:
            return False
        else:
            raise ValueError('Authorization server did not response an expecting value')

    except Exception as e:
        raise e


def require_rpt(fn):
    @wraps(fn)
    def _wrap(*args, **kwargs):
        if 'Authorization' not in request.headers:
            raise CustomError('Authorization header Required')

        auth = request.headers['Authorization']

        parts = auth.split()

        if len(parts) != 2:
            raise CustomError('Wrong context of Authorization Header')

        if parts[0].lower() != 'bearer':
            raise CustomError('Unsupported authorization type')

        # Inspect RPT
        f = validate_rpt(parts[1])

        if f is False:
            raise NotAuthorized('Invalid RPT', 401)

        # get key_for_rpt from database to decode RPT
        try:
            pass
            # payload = jwt.decode(parts[1], 'secret', algorithms=['HS256'])
        except jwt.InvalidTokenError as e:
            raise CustomError(repr(e), 403)

        return fn(*args, **kwargs)

    return _wrap