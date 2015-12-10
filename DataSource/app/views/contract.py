from flask_restful import Resource, reqparse
from app import api
from app.auth import require_token
from app.handler.dbHelper import DBHelper
from app.model.contract import Contract_Template
from app.handler.error_handler import NotAllowed

__author__ = 'xiao'


class ContractAPI(Resource):
    """
    Services Contract API
    """

    method_decorators = [require_token]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('Authorization', type=str, location='headers')
        super(ContractAPI, self).__init__()

    def post(self):
        raise NotAllowed()

    def put(self):
        raise NotAllowed()

    def delete(self):
        raise NotAllowed()

    def get(self):
        """
        Get contract
        :return: Object, services contract template
        """
        re = DBHelper.get_categories()
        ty = []
        for r in re:
            ty.append(r.name)
        Contract_Template['data_type'] = ty
        return Contract_Template, 200

    # def post(self):
    #     """
    #     Inform contract has been accepted
    #     :return: Object, resource sets of user owning
    #     """
    #     try:
    #         args = self.reqparse.parse_args()
    #         parts = args['Authorization'].split()
    #
    #         re = request.get_json()
    #
    #         if re.signature is True:
    #             register_resource_set(parts[1])
    #         else:
    #             return None
    #     except Exception as e:
    #         app_log.error(str(e), extra = {'sender': 'DataSource'})
    #         return None


api.add_resource(ContractAPI, '/contract', endpoint='contract')