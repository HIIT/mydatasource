import hashlib
from app import app
from flask import request
from flask_restful import Resource, reqparse
from app import api
from app.auth import require_token
from app.handler.dbHelper import DBHelper
from app.handler.error_handler import CustomError, NotAllowed


__author__ = 'Xiaoxiao.Xiong'


class UserAPI(Resource):
    """
    GET or Update users information
    """

    decorators = [require_token]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('Authorization', type=str, location='headers')
        super(UserAPI, self).__init__()

    def get(self):
        """
        get a specific user's information
        :return: Json
        """
        args = self.reqparse.parse_args()
        parts = args['Authorization'].split()
        info = DBHelper.get_info(parts[1])

        if info:
            return info
        else:
            raise CustomError('Invalid ext_id', status_code=400)

    def put(self):
        raise NotImplementedError()


    def post(self):
        raise NotAllowed()

    def delete(self):
        raise NotAllowed()


class RegisterAPI(Resource):
    """
    Register an user or an account to Data Source
    """
    def get(self):
        raise NotAllowed()

    def put(self):
        raise NotAllowed()

    def delete(self):
        raise NotAllowed()

    def post(self):
        """
        register a new account for user
        :return:
        """

        # if not request.json:
        #     raise InvalidUsage('Payload is not JSON', status_code=400)

        obj = request.get_json()
        # obj = {'username':'1', 'password':'2', 'email':'3'}

        if 'username' not in obj:
            raise CustomError('Parameter <username> missing', status_code=400)
        if 'password' not in obj:
            raise CustomError('Parameter <password> missing', status_code=400)
        if 'email' not in obj:
            raise CustomError('Parameter <email> missing', status_code=400)

        info = DBHelper.set_info(obj['email'])

        if DBHelper.check_username(obj['username']) is False:
            raise CustomError('register failed, username has existed!', status_code=409)

        ext_id = hashlib.md5(obj['username'] + '@' + app.config['APP_NAME']).hexdigest()

        obj = {
            'username': obj['username'],
            'password': obj['password'],
            'user_info_id': info,
            'status': 1,
            'ext_id': ext_id
        }

        account = DBHelper.set_user(obj)

        # app_log.info(('new user {0} registered').format(obj['username']), extra={'sender': 'DataSource'})

        return {
            'message': 'register successfully',
            'ext_id': account.ext_id,
            'status_code': 201
        }, 201


class AuthAPI(Resource):
    """
    Using username and password exchange ext_id
    """
    def get(self):
        raise NotAllowed()

    def put(self):
        raise NotAllowed()

    def delete(self):
        raise NotAllowed()

    def post(self):

        obj = request.get_json()
        # obj = {'username':'1', 'password':'2'}
        if 'username' not in obj:
            raise CustomError('Parameter <username> missing', status_code=400)
        if 'password' not in obj:
            raise CustomError('Parameter <password> missing', status_code=400)

        ext_id = DBHelper.get_ext_id(obj)

        if ext_id is None:
            raise CustomError('Invalid username or password!', status_code=400)

        return {
            'message': 'login successfully!',
            'ext_id': ext_id,
            'status_code': 200
        }, 200


api.add_resource(AuthAPI, '/auth', endpoint='login')
api.add_resource(RegisterAPI, '/user', endpoint='register')
api.add_resource(UserAPI, '/user/me', endpoint='profile')