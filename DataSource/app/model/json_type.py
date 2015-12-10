#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from app import db
import json


__author__ = 'Xiaoxiao.Xiong'

class JsonType(db.TypeDecorator):
    """
    Custom Type for Json Object
    """

    impl = db.Unicode

    def process_bind_param(self,value,engine):
        return unicode(json.dumps(value))

    def process_result_value(self,value,engine):
        if value:
            return json.loads(value)
        else:
            #defalut can also be a list
            return {}