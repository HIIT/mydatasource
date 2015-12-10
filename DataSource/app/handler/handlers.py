
"""
Expired
"""

from app.handler.dbHelper import DBHelper
import hashlib
from app import app
import urllib2
import json


__author__ = 'Xiaoxiao.Xiong'


def signup(obj):
    """
    Register an account
    :param obj: Json, {username:'', password:'', email:''}
    :return: Object, account/None
    """
    try:

        info = DBHelper.set_info(obj['email'])

        ext_id = hashlib.md5(obj['username'] + '@' + app.config['APP_NAME']).hexdigest()

        obj = {
            'username': obj['username'],
            'password': obj['password'],
            'user_info_id': info,
            'status': 1,
            'ext_id': ext_id
        }

        account = DBHelper.set_user(obj)

        if account is not None:
            return account
        else:
            return None

    except Exception as e:
        print(str(e))
        return None


def register_resource_set(ext_id):
    """
    register resource set to DataOperator
    :param ext_id: String, unique id
    :return: Boolean
    """
    try:
        user_id = DBHelper.get_user_id(ext_id)
        if user_id is False:
            return False

        rs = DBHelper.get_resource_set(user_id)

        for i in rs:
            data = json.dumps(i)
            req = urllib2.Request('http://46.101.30.187:8080/api/protection/resourceSets', data)
            req.add_header('Content-Type', 'application/json')

            f = urllib2.urlopen(req).read()
            obj = json.loads(f)

            con = obj['content'][0]

            DBHelper.set_rs_id({'name': con['name'], 'rs_id': con['rs_id']})
        return True
    except Exception as e:
        print(str(e))
        return None