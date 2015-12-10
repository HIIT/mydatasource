from flask_restful import Resource, reqparse
from app import api
from app.auth import require_rpt
from app.handler.dbHelper import DBHelper
from app.handler.error_handler import CustomError, NotAllowed

__author__ = 'Xiaoxiao.Xiong'


class ResourceAPI(Resource):
    """
    API for third-part services to request data with RPT
    """
    decorators = [require_rpt]

    def __init__(self):

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('rs_id', type=str, location='args', required=True)
        self.reqparse.add_argument('category', type=str, location='args')
        self.reqparse.add_argument('label', type=str, location='args')
        super(ResourceAPI, self).__init__()

    def get(self):
        """
        get resource from this specific DataSource
        :return: Json
        """
        args = self.reqparse.parse_args(strict=True)

        # if 'rs_id' not in args:
        #     raise CustomError('Parameter <rs_id> missing', status_code=400)

        rs_id = args['rs_id']

        if args['category'] is not None :
            category = args['category']
            if args['label'] is not None :
                label = args['label']
                data = DBHelper.get_data_by_rs_id(rs_id, category, label)
            else:
                data = DBHelper.get_data_by_rs_id(rs_id, category)

        else:

            data = DBHelper.get_data_by_rs_id(rs_id)

        if data is None:
            raise CustomError('No category has been registered in the resource set', status_code=200)
        else:
            # app_log.info(('{0} make a request for resource {1}').format('',rs_id), extra={'sender': 'DataSource'})
            return data, 200

    def put(self):
        raise NotAllowed()

    def post(self):
        raise NotAllowed()

    def delete(self):
        raise NotAllowed()

api.add_resource(ResourceAPI, '/resource', endpoint='resource')
# api.add_resource(ResourceAPI, '/resource/<code>', endpoint='resource')
# api.add_resource(ResourceAPI, '/resource/<code>/<category>', endpoint='resource')
# api.add_resource(ResourceAPI, '/resource/<code>/<category>/<label>', endpoint='resource')