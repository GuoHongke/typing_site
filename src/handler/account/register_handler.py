#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.sql import or_
from src.model.account_model import Account
from src.handler.base.base_handler import BaseHandler
from src.helper.verify_helper import VerifyHelper
from src.helper.md5_helper import Md5Helper
from src.utils import tools
from src.utils.logger import logger


class RegisterHandler(BaseHandler):
    def do_action(self, session):
        name = self.get_argument('name', None)
        password = self.get_argument('password', None)
        email = self.get_argument('email', None)
        error_msg = None
        if not all((name, password, email)):
            error_msg = u'请输入相关注册信息'
        if not error_msg and not VerifyHelper().name_check(name):
            error_msg = u'用户名格式错误'
        if not error_msg and not VerifyHelper().mail_check(email):
            error_msg = u'邮箱格式错误'
        if not error_msg:
            error_msg = VerifyHelper().password_verify(password)

        if not error_msg:
            try:
                account = session.query(Account.id).filter(or_(Account.name == name,
                                                               Account.email == email)).one_or_none()

                if not account:
                    account = Account(id=tools.unique_id('ad'), name=name, password=Md5Helper().ori_str_gen(password),
                                      email=email, lessons='[]')
                    session.add(account)
                    self.set_result({'name': account.name})
                elif account.name == name:
                    error_msg = u'用户名已被注册'
                else:
                    error_msg = u'邮箱已被注册'
            except Exception, e:
                logger.api_logger().api_error(e)
                error_msg = u'服务器错误'

        if error_msg:
            self.set_error(1, error_msg)
