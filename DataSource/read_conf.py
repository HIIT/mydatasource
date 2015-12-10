"""
    This script is aim to read config parameters from
    remote GenericConfig file.
"""

import json
import requests
from requests.auth import HTTPBasicAuth
from sets import Set

############### Service API #######################

# import DataSource API prefix(eg: http://127.0.0.1:10001/api/v0.1)
from app.config import DSOURCE_API

# HOSTNAME = 'http://127.0.0.1:10001/api/v0.1'

###################################################

def register_users(users):
    """
    register a new user
    :param users: JSON {username:"", password;"", email:""}
    :return: JSON Object {status_code:"", message;"", ext_id:""}
    """
    print 'register new users'
    for u in users:
        req = requests.post(DSOURCE_API+'/user', json=u)
        if not req.__bool__():
            print 'failed register'
        d = req.json()
        print json.dumps(d, indent=4)

def init_categories(categories):
    """
    init categories for this specific DataSource
    :param categories: JSON {name:"", desc;""}
    :return: JSON Object {status_code:"", message;""}
    """
    print json.dumps(categories, indent=4)
    for c in categories:
        req = requests.post(DSOURCE_API+'/category', json=c)
        if not req.__bool__():
            print 'failed create categories'
        data = req.json()
        print json.dumps(data, indent=4)


def init_units(units):
    """
    init units for this specific DataSource
    :param units: JSON {name:"", desc;""}
    :return: JSON Object {status_code:"", message;""}
    """
    print json.dumps(units, indent=4)
    for u in units:
        req = requests.post(DSOURCE_API+'/units', json=u)

        if not req.__bool__():
            print 'failed create units'
        data = req.json()
        print json.dumps(data, indent=4)


def init_label(labels):
    """
    init labels for this specific DataSource
    :param labels: JSON {name:"", desc;"", unit:"", category:""}
    :return: JSON Object {status_code:"", message;""}
    """
    print json.dumps(labels, indent=4)
    for lb in labels:
        req = requests.post(DSOURCE_API+'/label', json=lb)

        if not req.__bool__():
            print 'failed create label'
        data = req.json()
        print json.dumps(data, indent=4)


def read_conf():
    # read services' information from this specific DataSource
    print "get service's id"
    req = requests.get(DSOURCE_API+'/service_info')
    if not req.__bool__():
        print "failed get service's id"
    d = req.json()
    print json.dumps(d, indent=4)

    if 'service_id' not in d:
        print 'can not fetch service_id'
        return None

    service_id = d['service_id']
    config_uri = d['config_uri']
    auth_dop   = HTTPBasicAuth(d['config_username'], d['config_password'])


    # generate categories, units and labels from config file
    print 'read file'
    req = requests.get(config_uri, auth=auth_dop)

    if not req.__bool__():
        print 'failed read file'
        return None
    response = req.json()
    if 'sources' not in response:
        print 'can not fetch configuration from Generic_Config_File'
        return None
    else:
        if service_id not in response['sources']:
            print 'can not fetch <user_accounts> from configuration of source'
            return None
        conf = response['sources'][service_id]

    if 'user_accounts' not in conf:
        print 'can not fetch <user_accounts> from configuration of source'
        return None

    new_users = conf['user_accounts']

    if 'category_details' not in conf:
        print 'can not fetch <category_details> from configuration of source'
        return None

    ca = Set()
    un = Set()
    labels = []
    source_conf = conf['category_details']
    for i in source_conf:
        label = {
            'label': None,
            'units': None,
            'category': None,
            'desc': None
        }
        j = i.split('.')
        # get categories
        ca.add(j[0])
        # get units
        un.add(source_conf[i]['unit'])
        # init labels
        label['label'] = j[1]
        label['units'] = source_conf[i]['unit']
        label['category'] = j[0]
        labels.append(label)

    categories = []
    for c in ca:
        category = {
            'category': None,
            'desc': None
        }
        category['category'] = c
        categories.append(category)
    units = []
    for u in un:
        unit = {
            'units': None,
            'desc': None
        }
        unit['units'] = u
        units.append(unit)

    register_users(new_users)
    init_categories(categories)
    init_units(units)
    init_label(labels)

try:

    read_conf()
    # parser = argparse.ArgumentParser()
    # parser.add_argument('service_id', help="input service's id.")
    # args = parser.parse_args()
    # services_id = args.service_id
    # if services_id is not None:

    # register()
    # ext_id = login_profile()
    # services_id = get_services_id(ext_id)

except Exception as e:
    raise e
