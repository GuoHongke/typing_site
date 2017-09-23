#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.handler.base.base_handler import BaseHandler
from src.helper.login_helper import login_auth
from src.model import DBSession
from src.model.lessons_model import Lessons


class ListHandler(BaseHandler):
    @login_auth
    def do_action(self):
        session = DBSession()
        lessons = session.query(Lessons.id, Lessons.name, Lessons.file_id, Lessons.history_msg).filter(
            Lessons.account_id == self.account_id)
        lesson_list = []
        for lesson in lessons:
            _lesson = {
                'lesson_d': lesson.id,
                'name': Lessons.name,
                'file_id': Lessons.file_id
            }
            lesson_list.append(_lesson)

        self.set_result({
            'lesson_list': lesson_list
        })
