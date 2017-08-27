#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.handler.account.home_handler import HomeHandler

url_map = [
    (r'/', HomeHandler)
]
