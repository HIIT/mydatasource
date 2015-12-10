from flask import request
from flask_restful import Resource
from app import api
from app.handler.dbHelper import DBHelper
from app.handler.error_handler import CustomError, NotAllowed

__author__ = 'Xiaoxiao.Xiong'


class CategoryAPI(Resource):
    """
    Data classify for this specific DataSource
    """

    def __init__(self):
        super(CategoryAPI, self).__init__()

    def put(self):
        raise NotAllowed()

    def delete(self):
        raise NotAllowed()

    def get(self):
        """
        get all categories of this DataSource
        :return: Object
        """
        ca = DBHelper.get_categories()
        return ca, 200

    def post(self):
        """
        create a new category for this specific DataSource
        :return: JSON {message:"", status_code:""}
        """

        sample = request.get_json()

        if 'category' not in sample:
            raise CustomError('Parameter <category> missing', status_code=400)

        if DBHelper.get_category_by_name(sample['category']) is not None:
            raise CustomError(('{0} has been created').format(sample['category']), status_code=409)

        if 'desc' in sample:
            DBHelper.set_category(sample['category'],sample['desc'])
        else:
            DBHelper.set_category(sample['category'])

        return {
            'message': 'Created successfully!',
            'status_code': 201
        }, 201

api.add_resource(CategoryAPI, '/category', endpoint='category')