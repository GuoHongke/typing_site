#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.model.account_model import Account
from src.handler.base.base_handler import BaseHandler
from src.helper.verify_helper import VerifyHelper
from src.helper.md5_helper import Md5Helper
from src.utils import tools


class RegisterHandler(BaseHandler):
    def do_action(self, session):
        name = self.get_argument('name', None)
        password = self.get_argument('password', None)
        email = self.get_argument('email', None)

        error_msg = None
        if not all((name, password, email)):
            error_msg = u'请输入相关注册信息'
        print name, email, password
        if not error_msg and not VerifyHelper().name_check(name):
            error_msg = u'用户名格式错误'
        if not error_msg and not VerifyHelper().mail_check(email):
            error_msg = u'邮件格式错误'
        if not error_msg:
            error_msg = VerifyHelper().password_verify(password)

        if not error_msg:
            try:
                account = session.query(Account.id).filter(Account.name == name).one_or_none()

                if not account:
                    account = Account(id=tools.unique_id('ad'), name=name, password=Md5Helper().ori_str_gen(password),
                                      lessons='[]')
                    session.add(account)
                else:
                    error_msg = u'用户名已被注册'
            except Exception:
                error_msg = u'服务器错误'

        if error_msg:
            self.set_error(1, error_msg)
