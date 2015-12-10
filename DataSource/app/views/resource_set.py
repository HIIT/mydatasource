from flask import request
from flask_restful import Resource, reqparse
from app import api
from app.auth import require_token
from app.handler.dbHelper import DBHelper
from app.handler.error_handler import CustomError, NotAllowed

__author__ = 'Xiaoxiao.Xiong'


class ResourceSetAPI(Resource):
    """
    Resource Set
    """
    decorators = [require_token]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('Authorization', type=str, location='headers')
        super(ResourceSetAPI, self).__init__()

    def get(self):
        raise NotAllowed()

    def put(self):
        raise NotAllowed()

    def delete(self):
        raise NotAllowed()

    def post(self):
        """
        create a new resource set
        :return: JSON {message:"", status_code:""}
        """
        args = self.reqparse.parse_args()
        parts = args['Authorization'].split()
        user_id = DBHelper.get_user_id(parts[1])

        data = request.get_json()

        if not 'rs_id' or not 'categories' in data:
            raise CustomError('Invalid parameter, <rs_id> and <categories> required', status_code=400)

        if type(data['categories']) is not list:
            raise CustomError('the type of "categories" is a list', status_code=400)

        if DBHelper.check_rs_id(data['rs_id']) is not None:
            raise CustomError(('{0} has been created').format(data['rs_id']), status_code=409)

        DBHelper.set_resource_set(user_id, data['rs_id'], data['categories'])

        # app_log.info(('new resource set {0} created').format(data['rs_id']), extra={'sender': 'DataSource'})

        return {
            'message': 'Created successfully',
            'status_code': 201
        }, 201

api.add_resource(ResourceSetAPI, '/resource_set', endpoint='resource_set')