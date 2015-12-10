#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from app import db

__author__ = 'Xiaoxiao.Xiong'


class LinkRsData(db.Model):
    """
    Link resource set with categories
    """
    __tablename__ = 'LinkRsData'

    id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    resource_set_id = db.Column(db.Integer, db.ForeignKey('ResourceSet.id'), nullable=False)
    categories_id   = db.Column(db.Integer, db.ForeignKey('Categories.id'), nullable=False)

    resource_set = db.relationship('ResourceSet')
    categories   = db.relationship('Categories')

    def __init__(self, internal_rs_id, category_id):

        self.resource_set_id = internal_rs_id
        self.categories_id = category_id