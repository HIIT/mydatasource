from app import db, app_log
from app.handler.error_handler import NotFound
from app.model.city import City
from app.model.region import Region
from app.model.country import Country
from app.model.status import Status

from app.model.units import Units
from app.model.label import Label
from app.model.categories import Categories
from app.model.resource_set import ResourceSet
from app.model.receipt import Receipt
from app.model.data import Data
from app.model.link_rs_data import LinkRsData
from app.model.user_info import UserInfo
from app.model.user_account import UserAccount

__author__ = 'Xiaoxiao.Xiong'


class DBHelper(object):
    """
    Database handler, do CRUD
    """

    def __init__(self):
        pass

    @staticmethod
    def set_user(obj):
        """
        Insert a user account into table UserAccount.
        :param obj: Json, {username:'', password:''}
        :return: Object, if insert successfully return an instance of UserAccount , otherwise return None
        """
        try:
            user = UserAccount(**obj)
            db.session.add(user)
            db.session.commit()
            return user
        except Exception as e:
            db.session.rollback()
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def check_username(username):

        try:
            account = UserAccount.query.filter_by(username=username).first()
            if account is not None:
                return False
            else:
                return True
        except Exception as e:
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def get_ext_id(obj):
        """
        Check a user account.
        :param obj: Json, {username:'', password:''}
        :return: Object/String, if account existing return ext_id, otherwise return None
        """
        try:
            account = UserAccount.query.filter_by(username=obj['username']).first()
            if account is None:
                return None
            
            if account.password == obj['password']:
                return account.ext_id
            else:
                return None
        except Exception as e:
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def get_user_id(ext_id):
        """
        Get user_id via ext_id
        :param ext_id: String
        :return: Boolean/String
        """
        try:
            account = UserAccount.query.filter_by(ext_id=ext_id).first()
            if account is not None:
                return account.id
            else:
                return False
        except Exception as e:
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def check_token(ext_id):
        """
        Inspect whether ext_id is existing
        :param ext_id: String, unique identity, which like both OpenID and Token
        :return: Boolean if ext_id existing return True, otherwise return False
        """
        try:
            flag = UserAccount.query.filter_by(ext_id=ext_id).first()

            if flag is None or not flag:
                return False
            else:
                return True

        except Exception as e:
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def set_info(email):
        """
        Insert an info record into UserInfo table
        :param email: String
        :return:
        """
        try:
            obj = UserInfo.query.filter_by(email=email).first()
            if obj is not None:
                return obj
            else:
                info = UserInfo(email)
                db.session.add(info)
                db.session.commit()
                return info
        except Exception as e:
            db.session.rollback()
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def get_info(ext_id):
        """
        Get personal information
        :param ext_id: String, unique identity, which like both OpenID and Token
        :return: Object
        """
        try:
            user = UserAccount.query.filter_by(ext_id=ext_id).first()
            if user is not None:
                info = {
                    'email': user.user_info.email,
                    'firstName': user.user_info.firstName,
                    'lastName': user.user_info.lastName,
                    'gender': user.user_info.gender,
                    'address': user.user_info.address_1,
                    'city': user.user_info.city_id,
                    'region': user.user_info.region_id,
                    'country': user.user_info.country_id
                }
                return info
            else:
                return False
        except Exception as e:
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def update_info():
        """
        Update personal information
        :return: Boolean
        """
        try:
            pass
        except Exception as e:
            db.session.rollback()
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def set_receipt(receipt):
        """
        Insert a receipt record into Receipt table
        :param receipt: Object
        :return: Boolean
        """
        try:
            row = Receipt(**receipt)
            db.session.add(row)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def get_receipt():
        """
        Not to be used in this version
        Get receipt record from database
        :return:
        """
        try:
            pass
        except Exception as e:
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def update_receipt(obj):
        """
        Update the status of a consent receipt
        :param obj: Object, {'receipt_id':'','authorization_status':''}
        :return: Boolean
        """
        try:
            receipt = Receipt.query.filter_by(id=obj['receipt_id']).first()
            receipt.auth_status = obj['authorization_status']
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def get_resource_set(user_id):
        """
        Expired
        Get resource set of a specific user
        :param user_id: Int, unique id
        :return: Object,
        sample = [
            {
                "name":"Health",
                "categories":[
                    "Height",
                    "HeartRate"
                ]
            }
        ]
        """
        try:

            resource_sets = []
            # get all resource sets of this user
            rss = ResourceSet.query.filter_by(user_id=user_id).all()
            # get all categories of each resource set
            for rs in rss:
                s = {
                    'name': rs.name,
                    'categories': []
                }
                results = LinkRsData.query.filter_by(resource_set_id=rs.id).all()
                for row in results:
                    s['categories'].append(row.categories.name)

                resource_sets.append(s)

            return resource_sets

        except Exception as e:
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def set_resource_set(user_id, rs_id, categories):
        """
        Create a new resource set
        :param user_id Int
        :param rs_id String
        :param categories List
        :return: Boolean, True/False
        """
        try:
            rs = ResourceSet(user_id, rs_id)
            db.session.add(rs)

            for c in categories:
                c_obj = DBHelper.get_category_by_name(c)
                # can't find category in source server
                if c_obj is None:
                    raise NotFound(payload={'detail': ('can not find {0} in source').format(c)})
                lrd = LinkRsData(rs.id, c_obj.id)
                db.session.add(lrd)
            db.session.commit()
        except NotFound as e:
            db.session.rollback()
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e
        except Exception as e:
            db.session.rollback()
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def check_rs_id(rs_id):
        try:
            result = ResourceSet.query.filter_by(rs_id=rs_id).first()
            if result is not None:
                return result
            else:
                return None
        except Exception as e:
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def set_rs_id(obj):
        """
        Expired
        Mapping rs_id which generated by DOP with resource set
        :return: Boolean
        """
        try:
            rs = ResourceSet.query.filter_by(name=obj['name']).first()
            rs.rs_id = obj['rs_id']
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def get_data_by_rs_id(rs_id, category=None, label=None):
        """
        Get data by rs_id
        :param rs_id: generated by Data Operator for mapping resources set
        :param category: specific category
        :param label: specific label in category
        :return: JSON
        """
        try:
            # get user_id and resource_set_id by rs_id
            rs = ResourceSet.query.filter_by(rs_id=rs_id).first()
            if rs is None:
                raise NotFound(payload={'detail': ('Invalid parameter <rs_id>:{0}').format(rs_id)})

            user_id = rs.user_id
            resource_set_id = rs.id

            # whether specific an categoriess
            if category is not None:

                # get the id of this category
                ca = Categories.query.filter_by(name=category).first()
                if ca is None:
                    raise NotFound(payload={'detail': ('can not find {0} in source').format(category)})
                    # raise ValueError('Invalid parameter <category>')

                # whether resource has been registered
                u_ca = LinkRsData.query.filter(db.and_(
                    LinkRsData.resource_set_id == resource_set_id,
                    LinkRsData.categories_id == ca.id
                )).first()
                # if not, return None
                if u_ca is None:
                    raise NotFound(payload={
                        'detail': 'the category you request have not been registered in the resource set!'
                        })
                # if yes, return data
                # get all subsets of this category
                if label is not None:
                    lb = Label.query.filter(db.and_(
                        Label.c_id == ca.id,
                        Label.name == label
                    )).all()
                else:
                    lb = Label.query.filter_by(c_id=ca.id).all()

                data = []
                # get data
                for b in lb:
                    cd = Data.query.filter(db.and_(
                        Data.user_id == user_id,
                        Data.label_id == b.id
                    )).order_by(Data.timestamp).all()

                    if b.u_id is None:
                        temp_unit = None
                    else:
                        temp_unit = b.units.name

                    data.append({
                        'label': b.name,
                        'sample': [d.serialized for d in cd],
                        'units': temp_unit
                    })

                return {
                    'name': category,
                    'data': data
                }
            # if not specific categories
            # get all categories in this resource set
            ca = LinkRsData.query.filter_by(resource_set_id=resource_set_id).all()

            if ca is None:
                return None

            result = []

            # get user's data in this resource set by user_id and categories_id
            for i in ca:
                # get all labels of resource set
                lb = Label.query.filter_by(c_id=i.categories_id).all()
                data = []
                for b in lb:
                    cd = Data.query.filter(db.and_(
                        Data.user_id == user_id,
                        Data.label_id == b.id
                    )).order_by(Data.timestamp).all()
                    if b.u_id is None:
                        temp_unit = None
                    else:
                        temp_unit = b.units.name
                    data.append({
                        'label': b.name,
                        'sample': [d.serialized for d in cd],
                        'units': temp_unit
                    })
                result.append({
                    'name': i.categories.name,
                    'data': data
                })

            return result
        except NotFound as e:
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e
        except Exception as e:
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def set_category(name, desc=None):
        """
         Add a categories
        :param obj:{name:"",desc:""}
        :return:True/False
        """
        try:
            ca = Categories(name, desc)
            db.session.add(ca)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def get_categories():
        """
        Get categories list
        :return: Object
        """
        try:
            result = Categories.query.all()
            return result
        except Exception as e:
            app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def get_category_by_name(name):
        """
        Get id by categories name
        :return: id
        """
        try:
            result = Categories.query.filter_by(name=name).first()
            if result is not None:
                return result
            else:
                return None
        except Exception as e:
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def set_label(name, units_id, category_id, desc=None):
        """

        :param name:
        :param units_id:
        :param category_id:
        :param desc:
        :return:
        """
        try:
            lb = Label(name, units_id, category_id, desc)
            db.session.add(lb)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def get_labels():
        """
        Get label list
        :return: Object
        """
        try:
            result = Label.query.all()
            return result
        except Exception as e:
            app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def get_label_by_name(name):
        try:
            result = Label.query.filter_by(name=name).first()
            if result is not None:
                return result
            else:
                return None
        except Exception as e:
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def set_units(name, desc=None):
        """
        :param name:
        :param desc:
        :return:
        """
        try:
            ut = Units(name, desc)
            db.session.add(ut)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def get_units():
        try:
            result = Units.query.all()
            return result
        except Exception as e:
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def get_units_by_name(name):
        try:
            result = Units.query.filter_by(name=name).first()
            if result is not None:
                return result
            else:
                return None
        except Exception as e:
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def set_data(data):
        """
        Import data into database
        :param data:
        :return: Boolean
        """
        try:
            d = Data(**data)
            db.session.add(d)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e

    @staticmethod
    def get_data():
        try:
            pass
        except Exception as e:
            # app_log.error(repr(e), extra={'sender': 'DataSource'})
            raise e