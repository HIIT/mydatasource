#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from app import db

__author__ = 'Xiaoxiao.Xiong'

class Region(db.Model):
    """
    Region list
    """
    __tablename__  = 'Region'

    id      = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name    = db.Column(db.String(30), nullable=False)
    country = db.Column(db.Integer, db.ForeignKey('Country.id'), nullable=False)

    def __init__(self, name, country):
        self.name    = name
        self.country = country