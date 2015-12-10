#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from app.config import SERVICE_ID
from app.config import DSOURCE_API_ResourceSet

__author__ = 'Xiaoxiao.Xiong'


# Contract template is sent to DOP
Contract_Template = {
    "actor_id": SERVICE_ID,
    "endpoint_uri": DSOURCE_API_ResourceSet,
    "user_id": 201550803143023001,
    "status": "active",
    "created": "",
    "role": "Source",
    "legal_role": "controller",
    "contract_terms": "",
    "data_type": [
        "Food",
        "Pharmacy",
        "Fitness",
        "Health",
        "Finance",
        "Insurance"
    ],
    "intendet_use": [
        "free",
        "comm-sell",
        "com-keep",
        "annon-research"
    ],
    "validity_period": "auto_renew"
}
