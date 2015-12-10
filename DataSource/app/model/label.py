#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from app import db

__author__ = 'Xiaoxiao.Xiong'

class Label(db.Model):
    """
    Subset of Categories
    """
    __tablename__ = 'Label'

    id   = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    desc = db.Column(db.String(250), nullable=True)
    c_id = db.Column(db.Integer, db.ForeignKey('Categories.id'), nullable=False,)
    u_id = db.Column(db.Integer, db.ForeignKey('Units.id'), nullable=False,)

    units = db.relationship('Units')
    category = db.relationship('Categories')

    def __init__(self, name, units_id, category_id, desc=None):

        self.name = name
        self.desc = desc
        self.c_id = category_id
        self.u_id = units_id

    @property
    def serialized(self):
        """

        :return: object as a json format
        """
        return {
            'name': self.name,
            'desc': self.desc,
            'category': self.category.name,
            'units': self.units.name
        }

