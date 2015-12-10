from flask import request
from flask_restful import Resource
from app import api
from app.handler.dbHelper import DBHelper
from app.handler.error_handler import CustomError, NotAllowed

__author__ = 'Xiaoxiao.Xiong'


class UnitsAPI(Resource):
    """
    For users of DataSource, Get/Post data to DataSource
    """

    def __init__(self):
        super(UnitsAPI, self).__init__()

    def get(self):
        """
        create units from this specific DataSource
        :return: Object
        """
        ca = DBHelper.get_units()
        return ca, 200

    def post(self):
        """
        create a new units
        :return: Json {message:"", status_code:""}
        """

        sample = request.get_json()

        if 'units' not in sample:
            raise CustomError('Parameter <units> missing', status_code=400)

        if DBHelper.get_units_by_name(sample['units']) is not None:
            raise CustomError(('{0} has been created').format(sample['units']), status_code=409)

        if 'desc' in sample:
            DBHelper.set_units(sample['units'], sample['desc'])
        else:
            DBHelper.set_units(sample['units'])

        # app_log.info(('new unit {0} created').format(sample['units']), extra={'sender': 'DataSource'})
        return {
            'message': 'Created successfully!',
            'status_code': 201
        }, 201

    def put(self):
        raise NotAllowed()

    def delete(self):
        raise NotAllowed()

api.add_resource(UnitsAPI, '/units', endpoint='units')