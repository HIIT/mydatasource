from flask import request
from flask_restful import Resource, reqparse
from app import api
from app.auth import require_token
from app.handler.dbHelper import DBHelper
from app.handler.error_handler import CustomError, NotAllowed


__author__ = 'Xiaoxiao.Xiong'


class DataAPI(Resource):
    """
    For users of DataSource, Get/Post data to DataSource
    """
    decorators = [require_token]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('Authorization', type=str, location='headers')
        super(DataAPI, self).__init__()

    def get(self):
        raise NotImplementedError()
        # try:
        #     pass
        # except Exception as e:
        #     return None

    def post(self):
        """
        create new data
        :return:
        """
        args = self.reqparse.parse_args()
        parts = args['Authorization'].split()
        user_id = DBHelper.get_user_id(parts[1])

        sample = request.get_json()

        if 'label' not in sample:
            raise CustomError('Parameter <label> missing', status_code=400)
        if 'data' not in sample:
            raise CustomError('Parameter <data> missing', status_code=400)

        label = sample['label']
        data = sample['data']

        lb = DBHelper.get_label_by_name(label)
        if lb is None:
            raise CustomError('Label Not Found', status_code=404)
        label_id = lb.id

        for d in data:
            d.update({
                'user_id': user_id,
                'label_id': label_id
            })
            DBHelper.set_data(d)

        return {
                   'message': 'Upload successfully!',
                   'status_code': 201
               }, 201

    def put(self):
        raise NotAllowed()

    def delete(self):
        raise NotAllowed()

api.add_resource(DataAPI, '/data', endpoint='data')