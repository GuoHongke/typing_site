#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.handler.base.base_handler import BaseHandler
from src.model.account_model import Account
from src.helper.md5_helper import Md5Helper
from src.helper.verify_helper import VerifyHelper
from src.helper.login_helper import login_auth
from src.helper.error_msg_helper import Error
from src.utils.logger import logger


class UpdateHandler(BaseHandler):
    @login_auth
    def do_action(self, session):
        email = self.get_argument('email', None)
        name = self.get_argument('name', None)
        old_password = self.get_argument('old_password', None)
        new_password = self.get_argument('new_password', None)

        error_msg = None
        try:
            update_bag = {}
            if email:
                if VerifyHelper.mail_check(email):
                    if not session.query(Account.id).filter(Account.email == email).one_or_none():
                        update_bag['email'] = email
                    else:
                        error_msg = Error.DUPLICATE_MAIL
                else:
                    error_msg = Error.MAIL_ERROR

            if not error_msg and name:
                if VerifyHelper().name_check(name):
                    if not session.query(Account.id).filter(Account.name == name).one_or_none():
                        update_bag['name'] = name
                    else:
                        error_msg = Error.DUPLICATE_NAME
                else:
                    error_msg = Error.NAME_ERROR

            if not error_msg and new_password and old_password:
                if new_password == old_password:
                    error_msg = Error.NEW_PWD_ERROR
                else:
                    account = session.query(Account.password).filter(Account.id == self.account_id).one_or_none()
                    if account and Md5Helper.key_gen(old_password) == account.password:
                        error_msg = VerifyHelper().password_verify(new_password)
                    if not error_msg:
                        update_bag['password'] = Md5Helper.key_gen(new_password)

            if not error_msg and update_bag is not {}:
                session.query(Account).filter(Account.id == self.account_id).update(update_bag)
        except Exception, e:
            logger.api_logger().api_error(e)
            error_msg = Error.SERVER_ERROR

        if error_msg:
            self.set_error(1, error_msg)


