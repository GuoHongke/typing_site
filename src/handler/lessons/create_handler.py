#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.handler.base.base_handler import BaseHandler
from src.model.lessons_model import Lessons
from sqlalchemy.sql import exists
from src.utils import tools
from src.helper.login_helper import login_auth


class LessonCreateHandler(BaseHandler):
    @login_auth
    def do_action(self, session):
        error_msg = None
        lesson_name = self.get_argument('lesson_name', None)
        if not error_msg and not lesson_name:
            error_msg = u'课程名不能为空'

        if not error_msg:
            try:
                lesson = session.query(exists().where(Lessons.name == lesson_name)).scalar()

                if lesson:
                    self.set_error(1, u'课程名已存在')
                else:
                    new_ld = tools.unique_id('ld')
                    new_lesson = Lessons(id=new_ld, name=lesson_name, account_id=self.account_id, file_ids='[]')
                    session.add(new_lesson)
            except Exception:
                error_msg = u"服务器内部错误"

        if error_msg:
            self.set_error(1, error_msg)
