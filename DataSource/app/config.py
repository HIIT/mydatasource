#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

__author__ = 'Xiaoxiao.Xiong'

import os
import urllib2, base64
import json

ABS_PATH = os.path.dirname(os.path.abspath(__file__))

SQLALCHEMY_COMMIT_ON_TEARDOWN = True

################### edit config before running app #############################

OPERATOR_ID = '1'

SERVICE_ID = '1'

SECRET_KEY = 'dataSource'

SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://dsource:123456@localhost/datasource'

CONFIG_URI = 'http://178.62.244.150:8080/config'
CONFIG_USERNAME = 'testuser'
CONFIG_PASSWORD = 'Hello'

#################### READ REMOTE CONFIG ########################################

try:

    request = urllib2.Request(CONFIG_URI)
    base64string = base64.encodestring('%s:%s' % (CONFIG_USERNAME, CONFIG_PASSWORD)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    result = urllib2.urlopen(request)
    response = json.loads(result.read())

    if not 'sources' or not 'operators' in response:
        print 'can not fetch <source> or <operators> configuration from Generic_Config_File'
    else:
        if SERVICE_ID not in response['sources']:
            print 'can not fetch <user_accounts> from configuration of source'
        source = response['sources'][SERVICE_ID]
        operator = response['operators'][OPERATOR_ID]

except Exception as e:
    print repr(e)
    exit()


############################## END READ #################################

try:

    APP_NAME = source['name']
    APP_PORT = source['network']['port_api']

    DSOURCE_API = 'http://' + source['network']['ip_public'] + ':' + str(APP_PORT) +'/api/v0.1'

    DSOURCE_API_ResourceSet = DSOURCE_API +'/resource_set'

    DOP_API_RPT = 'http://' + operator['network']['ip_public'] \
                  + ':' + operator['network']['port_api'] \
                  + operator['endpoints'][0]['RPT_introspection_endpoint']

except Exception as e:
    print repr(e)
    exit()
