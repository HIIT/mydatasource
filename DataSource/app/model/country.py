#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from app import db

__author__ = 'Xiaoxiao.Xiong'

class Country(db.Model):
    """
    Country list
    """
    __tablename__  = 'Country'

    id   = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self,name):

        self.name = name

