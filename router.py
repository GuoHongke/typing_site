#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.handler.account.home_handler import HomeHandler
from src.handler.account.file_handler import FileHandler


url_map = [
    (r'/', HomeHandler),
    (r'/file', FileHandler)
]
