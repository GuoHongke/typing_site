#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.utils import config
from src.handler.base.base_handler import BaseHandler
from src.model.account_model import Account
from src.helper.md5_helper import Md5Helper
from src.helper.error_msg_helper import Error
from sqlalchemy import and_, or_


class LoginHandler(BaseHandler):
    def do_action(self, session):
        login_card = self.get_argument('login_card', None)
        password = self.get_argument('password', None)
        error_msg = ''
        if not login_card:
            error_msg = Error.NO_LOGIN_CARD
        elif not password:
            error_msg = Error.NO_PASSWORD

        if not error_msg:
            gen_password = Md5Helper().ori_str_gen(password)
            account = session.query(Account.id, Account.name).filter(and_(
                or_(Account.email == login_card, Account.name == login_card),
                Account.password == gen_password)).one_or_none()
            if account:
                cookie_expire_time = int(config.get('global', 'cookie_expire_time'))
                domain = config.get('global', 'domain')
                self.set_secure_cookie("account_id", account.id, domain=domain, expires_days=cookie_expire_time)
                self.set_result({
                    'name': account.name,
                    'email': account.email
                })
            else:
                error_msg = Error.LOGIN_ERROR

        if error_msg:
            self.set_error(1, error_msg)
