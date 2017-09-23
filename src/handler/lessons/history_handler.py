#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.handler.base.base_handler import BaseHandler
from src.helper.login_helper import login_auth


class HistoryHandler(BaseHandler):
    @login_auth
    def do_action(self):
        pass