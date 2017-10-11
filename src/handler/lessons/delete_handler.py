#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.sql import and_
from src.handler.base.base_handler import BaseHandler
from src.model.lessons_model import Lessons
from src.helper.login_helper import login_auth
from src.helper.error_msg_helper import Error
from src.utils.logger import logger


class LessonDeleteHandler(BaseHandler):
    @login_auth
    def do_action(self, session):
        error_msg = None
        lesson_id = self.get_argument('lesson_id', ' ')
        try:
            if not session.query(Lessons).filter(and_(Lessons.account_id == self.account_id,
                                                      Lessons.id == lesson_id)).delete():
                error_msg = Error.NO_LESSON
        except Exception, e:
            logger.api_logger().api_error(e)
            error_msg = Error.SERVER_ERROR

        if error_msg:
            self.set_error(1, error_msg)

