from flask import request
from flask_restful import Resource
from app import api
from app.handler.dbHelper import DBHelper
from app.handler.error_handler import CustomError, NotFound, NotAllowed

__author__ = 'Xiaoxiao.Xiong'


class LabelAPI(Resource):
    """
    For users of DataSource, Get/Post data to DataSource
    """

    def __init__(self):
        super(LabelAPI, self).__init__()

    def get(self):
        """
        create labels of this specific DataSource
        :return: Object
        """
        lbs = DBHelper.get_labels()
        return lbs,201

    def post(self):
        """
        create a new label for this specific DataSource
        :return: JSON {message:"", status_code:""}
        """
        sample = request.get_json()

        if 'label' not in sample:
            raise CustomError('Parameter <label> missing', status_code=400)
        if 'units' not in sample:
            raise CustomError('Parameter <units> missing', status_code=400)
        if 'category' not in sample:
            raise CustomError('Parameter <category> missing', status_code=400)

        label = sample['label']
        units = sample['units']
        category = sample['category']

        if DBHelper.get_label_by_name(label) is not None:
            raise CustomError(('{0} has been created').format(label), status_code=409)

        if units is None:
            u_id = None
        else:
            un = DBHelper.get_units_by_name(units)
            if un is None:
                raise NotFound(payload={'detail': ('{0} Not Found').format(units)})
            u_id = un.id

        ca = DBHelper.get_category_by_name(category)
        if ca is None:
            raise NotFound(payload={'detail': ('{0} Not Found').format(category)})

        if 'desc' in sample:
            DBHelper.set_label(label, u_id, ca.id, sample['desc'])
        else:
            DBHelper.set_label(label, u_id, ca.id)
        return {
            'message': 'Upload successfully!',
            'status_code': 201
        }, 201

    def put(self):
        raise NotAllowed()

    def delete(self):
        raise NotAllowed()

api.add_resource(LabelAPI, '/label', endpoint='label')