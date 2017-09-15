#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from src.handler.base.base_handler import BaseHandler
from src.model import DBSession
from src.model.lessons_model import Lessons


class HomeHandler(BaseHandler):
    def do_action(self):
        session = DBSession()
        lessons = session.query(Lessons.id, Lessons.name, Lessons.file_ids).yield_per(100).limit(1000000)

        lesson_list = []
        for lesson in lessons:
            res = {
                'id': lesson.id,
                'name': lesson.name,
                'file_ids': json.loads(lesson.file_ids)
            }
            lesson_list.append(res)
        result = {
            'msg': 'Welcome to the typing site!',
            'lesson_list': lesson_list
        }
        self.set_result(result)
