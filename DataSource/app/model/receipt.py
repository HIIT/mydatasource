#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from app import db
from json_type import JsonType

__author__ = 'Xiaoxiao.Xiong'

class Receipt(db.Model):
    """
    Consent receipt
    """
    __tablename__  = 'Receipt'

    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    receipt_id  = db.Column(db.String(50),nullable=True)
    contract_id = db.Column(db.String(50),nullable=True)
    account_id  = db.Column(db.String(100),nullable=True)
    rs_id       = db.Column(db.String(100),nullable=True)
    key_rpt     = db.Column(db.String(200),nullable=True)
    auth_status = db.Column(db.String(50),nullable=True)
    summary = db.Column(JsonType(500),nullable=True)

    def __init__(self, **kwargs):

        self.receipt_id    = kwargs['consent_receipt_id']
        self.contract_id   = kwargs['service_contract_id']
        self.account_id    = kwargs['account_id']
        self.rs_id         = kwargs['rs_id']
        self.key_rpt       = kwargs['key_used_to_sign_rpt']
        self.auth_status   = kwargs['authorization_status']
        self.summary       = kwargs['consent_summary']