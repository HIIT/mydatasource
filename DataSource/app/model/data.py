#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from app import db

__author__ = 'Xiaoxiao.Xiong'


class Data(db.Model):
    """
    Users' data
    """
    __tablename__ = 'Data'

    id        = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id   = db.Column(db.Integer, db.ForeignKey('UserAccount.id'), nullable=False)
    timestamp = db.Column(db.String(50), nullable=True)
    value     = db.Column(db.String(50), nullable=True)
    label_id  = db.Column(db.Integer, db.ForeignKey('Label.id'), nullable=False)

    user = db.relationship('UserAccount')
    label = db.relationship('Label')

    def __init__(self, **kwargs):

        self.user_id   = kwargs['user_id']
        self.timestamp = kwargs['timestamp']
        self.value     = kwargs['value']
        self.label_id  = kwargs['label_id']

    @property
    def serialized(self):
        """

        :return: object data as a json format
        """
        return {
            'timestamp': self.timestamp,
            'value': self.value
        }