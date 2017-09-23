#!/usr/bin/env python
# -*- coding: utf-8 -*-


def login_auth(func):
    def _auth(handler):
        if not handler.account_id:
            handler.set_error(1, u'请先完成登录')
            return
        else:
            func(handler)
    return _auth
