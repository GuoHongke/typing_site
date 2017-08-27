#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.handler.base.base_handler import BaseHandler


class HomeHandler(BaseHandler):
    def do_action(self):
        result = {'msg': 'Welcome to the typing site!'}
        self.set_result(result)
