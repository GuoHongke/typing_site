#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.utils import config
from src.handler.base.base_handler import BaseHandler
from src.model.account_model import Account
from src.helper.md5_helper import Md5Helper
from sqlalchemy import and_, or_


class LoginHandler(BaseHandler):
    def do_action(self, session):
        login_card = self.get_argument('login_card', None)
        password = self.get_argument('password', None)

        error_msg = ''
        if not login_card:
            error_msg = u'请输入登录名'
        elif not password:
            error_msg = u'请输入密码'

        if not error_msg:
            gen_password = Md5Helper().ori_str_gen(password)
            account = session.query(Account.id, Account.name).filter(and_(
                or_(Account.email == login_card, Account.name == login_card),
                Account.password == gen_password)).one_or_none()
            session.close()
            if account:
                cookie_expire_time = int(config.get('global', 'cookie_expire_time'))
                self.set_secure_cookie("account_id", account.id, expires_days=cookie_expire_time)
                self.set_result({'name': account.name})
            else:
                error_msg = u'登录名或密码错误'

        if error_msg:
            self.set_error(1, error_msg)
