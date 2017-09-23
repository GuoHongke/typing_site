#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.handler.base.base_handler import BaseHandler
from src.model import DBSession
from src.model.lessons_model import Lessons


class HomeHandler(BaseHandler):
    def do_action(self):
        session = DBSession()
        lessons = session.query(Lessons.id, Lessons.name, Lessons.file_id).filter(
            Lessons.account_id == '1').yield_per(100).limit(1000000)

        lesson_list = []
        for lesson in lessons:
            res = {
                'id': lesson.id,
                'name': lesson.name,
                'file_id': lesson.file_id
            }
            lesson_list.append(res)
        result = {
            'lesson_list': lesson_list
        }
        self.set_result(result)