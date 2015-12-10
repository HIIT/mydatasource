#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from app import db

__author__ = 'Xiaoxiao.Xiong'

class Status(db.Model):
    """
    account status
    """
    __tablename__  = 'Status'

    id   = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30),nullable=False)
    desc = db.Column(db.String(250),nullable=True)

    def __init__(self, name, desc=None):

        self.name = name
        self.desc = desc

