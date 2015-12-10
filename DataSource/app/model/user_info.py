#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from app import db

__author__ = 'Xiaoxiao.Xiong'


class UserInfo(db.Model):
    """
    User Information
    """
    __tablename__ = 'UserInfo'

    id        = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email     = db.Column(db.String(50), nullable=False)
    gender    = db.Column(db.String(10), nullable=True)
    address_1 = db.Column(db.String(100), nullable=True)
    address_2 = db.Column(db.String(100), nullable=True)
    firstName = db.Column(db.String(50), nullable=True)
    lastName  = db.Column(db.String(50), nullable=True)

    city_id    = db.Column(db.Integer, db.ForeignKey('City.id'))
    region_id  = db.Column(db.Integer, db.ForeignKey('Region.id'))
    country_id = db.Column(db.Integer, db.ForeignKey('Country.id'))

    city = db.relationship('City')
    region = db.relationship('Region')
    country = db.relationship('Country')

    def __init__(self, email):

        self.email      = email
        self.gender     = None
        self.city_id    = None
        self.region_id  = None
        self.country_id = None
        self.address_1  = None
        self.address_2  = None
        self.firstName  = None
        self.lastName   = None