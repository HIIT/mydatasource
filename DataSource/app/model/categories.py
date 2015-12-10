#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from app import db

__author__ = 'Xiaoxiao.Xiong'


class Categories(db.Model):
    """
    Label classification
    """

    __tablename__ = 'Categories'

    id       = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name     = db.Column(db.String(50), nullable=False)
    desc     = db.Column(db.String(250), nullable=True)

    def __init__(self, name, desc=None):
        """
        init a record
        :param name: category name
        :param desc: the description of this category
        """

        self.name = name
        self.desc = desc