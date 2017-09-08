#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from src.handler.base.base_handler import BaseHandler
from src.model import DBSession
from src.model.files_model import Files


class FileHandler(BaseHandler):
    def do_action(self):
        file_id = self.get_argument('file_id', None)
        session = DBSession()
        try:
            _file = session.query(Files).filter(Files.id == file_id).one()
            cur_dir = os.path.dirname(os.path.realpath(__file__))
            resources_dir = os.path.join(cur_dir, "../../../resources")
            file_path = os.path.join(resources_dir, _file.name)
            with open(file_path, 'r') as rf:
                file_msg = ''.join(rf.readlines())
                result = {
                    'file_msg': file_msg
                }
                self.set_result(result)
        except Exception:
            self.set_error(1, 'Read file error')
