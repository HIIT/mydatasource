#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from app import app

# import port number from app/config.py
from app.config import APP_PORT

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(APP_PORT), debug='false')