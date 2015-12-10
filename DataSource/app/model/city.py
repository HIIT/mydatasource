#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from app import db

__author__ = 'Xiaoxiao.Xiong'


class City(db.Model):
    """
    City list
    """
    __tablename__ = 'City'

    id     = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name   = db.Column(db.String(50), nullable=False)
    region = db.Column(db.Integer, db.ForeignKey('Region.id'), nullable=False)

    def __init__(self, name, region):
        self.name   = name
        self.region = region