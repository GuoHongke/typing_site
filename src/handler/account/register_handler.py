#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from sqlalchemy.sql import or_
from src.model.account_model import Account
from src.handler.base.base_handler import BaseHandler
from src.helper.verify_helper import VerifyHelper
from src.helper.md5_helper import Md5Helper
from src.helper.error_msg_helper import Error
from src.utils import tools
from src.utils import config
from src.utils.logger import logger


class RegisterHandler(BaseHandler):
    def do_action(self, session):
        name = self.get_argument('name', None)
        password = self.get_argument('password', None)
        email = self.get_argument('email', None)
        error_msg = None
        if not all((name, password, email)):
            error_msg = Error.NO_REGISTER_ARGS
        if not error_msg and not VerifyHelper().name_check(name):
            error_msg = Error.NAME_ERROR
        if not error_msg and not VerifyHelper().mail_check(email):
            error_msg = Error.MAIL_ERROR
        if not error_msg:
            error_msg = VerifyHelper().password_verify(password)

        if not error_msg:
            try:
                account = session.query(Account.id).filter(or_(Account.name == name,
                                                               Account.email == email)).one_or_none()

                if not account:
                    create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    account = Account(id=tools.unique_id('ad'), name=name, password=Md5Helper().ori_str_gen(password),
                                      email=email, create_time=create_time)
                    session.add(account)
                    cookie_expire_time = int(config.get('global', 'cookie_expire_time'))
                    domain = config.get('global', 'domain')
                    self.set_secure_cookie("account_id", account.id, domain=domain, expires_days=cookie_expire_time)
                    self.set_result({{
                        'name': account.name,
                        'email': account.email
                    }})

                elif account.name == name:
                    error_msg = Error.DUPLICATE_NAME
                else:
                    error_msg = Error.DUPLICATE_MAIL
            except Exception, e:
                logger.api_logger().api_error(e)
                error_msg = Error.SERVER_ERROR

        if error_msg:
            self.set_error(1, error_msg)
