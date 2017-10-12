#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.handler.base.base_handler import BaseHandler
from src.model.account_model import Account
from src.helper.error_msg_helper import Error
from src.helper.login_helper import login_auth
from src.utils.logger import logger


class ShowHandler(BaseHandler):
    @login_auth
    def do_action(self, session):
        try:
            account = session.query(Account.name, Account.email).filter(Account.id == self.account_id).one_or_onne()
            if account:
                show = {
                    'name': account.name,
                    'email': account.email
                }
                self.set_result({
                    'show': show
                })
        except Exception, e:
            logger.api_logger().api_error(e)
            self.set_error(1, Error.SERVER_ERROR)