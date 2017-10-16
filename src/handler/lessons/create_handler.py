#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from sqlalchemy.sql import and_
from src.handler.base.base_handler import BaseHandler
from src.model.lessons_model import Lessons
from src.model.files_model import Files
from src.utils import tools
from src.utils.logger import logger
from src.helper.login_helper import login_auth
from src.helper.error_msg_helper import Error


class LessonCreateHandler(BaseHandler):
    @login_auth
    def do_action(self, session):
        error_msg = None
        lesson_name = self.get_argument('lesson_name', None)
        file_id = self.get_argument('file_id', None)
        notes = self.get_argument('notes', None)
        if not error_msg and not lesson_name:
            error_msg = Error.NO_LESSON_NAME
        if not error_msg and not file_id:
            error_msg = Error.LESSON_NO_FILE
        if not error_msg:
            try:
                if session.query(Lessons).filter(and_(Lessons.name == lesson_name,
                                                      Lessons.account_id == self.account_id)).one_or_none():
                    error_msg = Error.DUPLICATE_LESSON
                elif not session.query(Files).filter(Files.id == file_id).one_or_none():
                    error_msg = Error.NO_FILE
                else:
                    new_ld = tools.unique_id('ld')
                    create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    new_lesson = Lessons(id=new_ld, name=lesson_name, account_id=self.account_id,
                                         file_id=file_id, create_time=create_time, notes=notes)
                    session.add(new_lesson)
            except Exception, e:
                logger.api_logger().api_error(e)
                error_msg = Error.SERVER_ERROR

        if error_msg:
            self.set_error(1, error_msg)
