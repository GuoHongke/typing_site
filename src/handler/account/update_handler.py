#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.handler.base.base_handler import BaseHandler
from src.model.account_model import Account
from src.helper.md5_helper import Md5Helper
from src.helper.verify_helper import VerifyHelper
from src.helper.login_helper import login_auth
from src.utils.logger import logger


class UpdateHandle(BaseHandler):
    @login_auth
    def do_action(self, session):
        email = self.get_argument('email', None)
        old_password = self.get_argument('old_password', None)
        new_password = self.get_argument('new_password', None)

        error_msg = None
        try:
            if email:
                if VerifyHelper.mail_check(email):
                    if not session.query(Account.id).filter(Account.email == email).one_or_none():
                        session.query(Account).filter(Account.id == self.account_id).update({'email': email})
                    else:
                        error_msg = u'邮箱已被注册'
                else:
                    error_msg = u'邮箱格式错误'

            if new_password and old_password:
                account = session.query(Account.password).filter(Account.id == self.account_id).one_or_none()
                if account and Md5Helper.key_gen(old_password) == account.password:
                    error_msg = VerifyHelper().password_verify(new_password)
                if not error_msg:
                    md5_password = Md5Helper.key_gen(new_password)
                    session.query(Account).filter(Account.id == self.account_id).update({'password': md5_password})
        except Exception, e:
            logger.api_logger().api_error(e)
            error_msg = u'服务器异常'

        if error_msg:
            self.set_error(1, error_msg)


