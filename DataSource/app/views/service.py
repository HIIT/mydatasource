from flask_restful import Resource
from app import api
from app.config import SERVICE_ID,APP_NAME, CONFIG_URI, CONFIG_USERNAME, CONFIG_PASSWORD
from app.handler.error_handler import NotAllowed

__author__ = 'Xiaoxiao.Xiong'


class ServiceAPI(Resource):
    """
    show service's status
    """

    def __init__(self):
        super(ServiceAPI, self).__init__()

    def get(self):
        detail = {
            'service_id':SERVICE_ID,
            'service_name':APP_NAME,
            'config_uri':CONFIG_URI,
            'config_username':CONFIG_USERNAME,
            'config_password':CONFIG_PASSWORD,
        }
        return detail,200

    def post(self):
        raise NotAllowed()

    def put(self):
        raise NotAllowed()

    def delete(self):
        raise NotAllowed()

class ServiceStatusAPI(Resource):
    """
    show service's status
    """

    def __init__(self):
        super(ServiceStatusAPI, self).__init__()

    def get(self):
        detail = {
            'status':'ok'
        }
        return detail,200

    def post(self):
        raise NotAllowed()

    def put(self):
        raise NotAllowed()

    def delete(self):
        raise NotAllowed()

api.add_resource(ServiceAPI, '/service_info', endpoint='info')
api.add_resource(ServiceStatusAPI, '/status', endpoint='status')