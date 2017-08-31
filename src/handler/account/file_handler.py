#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.handler.base.base_handler import BaseHandler
from src.model import DBSession
from src.model.files_model import Files


class FileHandler(BaseHandler):
    def do_action(self):
        file_id = self.get_argument('file_id', None)
        session = DBSession()
        file_msg = session.query(Files).filter(Files.id == file_id).one()

        result = {
            'msg': 'Welcome to the typing site!',
            'file_msg': file_msg.name
        }

        self.set_result(result)
