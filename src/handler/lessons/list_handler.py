#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.handler.base.base_handler import BaseHandler
from src.model.lessons_model import Lessons
from src.utils.logger import logger
from src.helper.error_msg_helper import Error


class LessonListHandler(BaseHandler):
    def do_action(self, session):
        user = self.get_argument('user', None)

        if user and self.account_id:
            account_id = self.account_id
        else:
            account_id = '1'
        try:
            lessons = session.query(Lessons.id, Lessons.name, Lessons.file_id).filter(
                Lessons.account_id == account_id)
            lesson_list = []
            for lesson in lessons:
                _lesson = {
                    'lesson_d': lesson.id,
                    'name': lesson.name,
                    'file_id': lesson.file_id
                }
                lesson_list.append(_lesson)
            self.set_result({
                'lesson_list': lesson_list
            })
        except Exception, e:
            logger.api_logger().api_error(e)
            self.set_error(1, Error.SERVER_ERROR)
