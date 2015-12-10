from flask import request
from flask_restful import Resource
from app import api
from app.auth import require_token
from app.handler.dbHelper import DBHelper
from app.handler.error_handler import CustomError, NotAllowed

__author__ = 'Xiaoxiao.Xiong'


class ReceiptAPI(Resource):
    """
    Consent Receipt API
    """

    method_decorators = [require_token]

    def get(self):
        raise NotAllowed()

    def delete(self):
        raise NotAllowed()

    def post(self):
        """
        Store consent receipt
        :return:
        """
        sample = request.get_json()
        if 'consentReceipt' not in sample:
            return CustomError('No consentReceipt in payload', status_code=400)

        receipt = sample['consentReceipt']
        DBHelper.set_receipt(receipt)
        return {'message': 'Accepted!'}, 201


    def put(self):
        """
        Update the status of consent receipt
        :return:
        """
        sample = request.get_json()
        if 'receipt_id' not in sample:
            return CustomError('No receipt_id in payload', status_code=400)
        if 'authorization_status' not in sample:
            return CustomError('No authorization_status in payload', status_code=400)

        DBHelper.update_receipt(sample)
        return {'message': 'updated!'}, 200


api.add_resource(ReceiptAPI, '/receipt', endpoint='receipt')
