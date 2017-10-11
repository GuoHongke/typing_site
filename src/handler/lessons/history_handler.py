#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.handler.base.base_handler import BaseHandler
from src.model.history_model import History
from src.utils.logger import logger
from src.helper.error_msg_helper import Error


class HistoryHandler(BaseHandler):
    def do_action(self, session):
        try:
            history_list = session.query(History.lesson_id, History.history_msg).filter(
                History.account_id == self.account_id)
            history = []
            for h in history_list:
                _h = {
                    'lesson_id': h.lesson_id,
                    'history_msg': h.history_msg
                }
                history.append(_h)

            self.set_result({
                'history': history
            })
        except Exception, e:
            logger.api_logger().api_error(e)
            self.set_error(1, Error.SERVER_ERROR)