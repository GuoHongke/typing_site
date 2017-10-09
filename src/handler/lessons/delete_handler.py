#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.sql import and_
from src.handler.base.base_handler import BaseHandler
from src.model.lessons_model import Lessons
from src.helper.login_helper import login_auth


class LessonDeleteHandler(BaseHandler):
    @login_auth
    def do_action(self, session):
        error_msg = None
        lesson_id = self.get_argument('lesson_id', ' ')
        if not session.query(Lessons).filter(and_(Lessons.account_id == self.account_id,
                                                  Lessons.id == lesson_id)).delete():
            error_msg = u'删除失败'

        if error_msg:
            self.set_error()

