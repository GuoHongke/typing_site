#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
from sqlalchemy.sql import and_
from src.handler.base.base_handler import BaseHandler
from src.model.history_model import History
from src.helper.login_helper import login_auth
from src.helper.error_msg_helper import Error
from src.utils.logger import logger


class LessonSaveHandler(BaseHandler):
    @login_auth
    def do_action(self, session):
        lesson_id = self.get_argument('lesson_id', None)
        page_id = int(self.get_argument('page_id', 0))
        wpm = int(self.get_argument('wpm', 0))
        invalid_rate = float(self.get_argument('invalid_rate', 0.0))
        error_array = self.get_argument('error_array', [])

        error_msg = None
        if lesson_id:
            new_page = {
                'page_id': page_id,
                'wpm': wpm,
                'invalid_rate': invalid_rate,
                'update_time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
                'error_array': error_array
            }
            history_msg = []
            try:
                history = session.query(History.history_msg).filter(and_(History.account_id == self.account_id,
                                                                         History.lesson_id == lesson_id)).one_or_none()
                if history:
                    history_msg = json.loads(history.history_msg)
                    history_msg.append(new_page)
                    session.query(History).filter(and_(History.account_id == self.account_id,
                                                       History.lesson_id == lesson_id)).update(
                        {'history_msg': json.dumps(history_msg)})
                else:
                    history_msg.append(new_page)
                    new_history = History(account_id=self.account_id, lesson_id=lesson_id,
                                          history_msg=json.dumps(history_msg))
                    session.add(new_history)
            except Exception, e:
                logger.api_logger().api_error(e)
                error_msg = Error.SERVER_ERROR
        else:
            error_msg = Error.NO_LESSON_ID

        if error_msg:
            self.set_error(1, error_msg)
