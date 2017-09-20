#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from src.handler.base.base_handler import BaseHandler
from src.model import DBSession
from src.model.files_model import Files
from src.helper.redis_helper import RedisClient


class FileHandler(BaseHandler):
    def do_action(self):
        file_id = self.get_argument('file_id', None)
        page_id = int(self.get_argument('page_id', 0))
        session = DBSession()
        redis_client = RedisClient().connect()

        try:
            _file = session.query(Files.name).filter(Files.id == file_id).one()
            file_cache = redis_client.hgetall(_file.name)

            if file_cache:
                file_lines = json.loads(file_cache['file_msg_all'])
                pages = int(file_cache['pages'])
            else:
                cur_dir = os.path.dirname(os.path.realpath(__file__))
                resources_dir = os.path.join(cur_dir, "../../../resources")
                file_path = os.path.join(resources_dir, _file.name)
                with open(file_path, 'r') as rf:
                    file_lines = rf.readlines()
                    pages = int(round(float(len(file_lines)) / 20 + 0.5))
                    redis_client.hmset(_file.name, {'file_msg_all': json.dumps(file_lines), 'pages': pages})

            if pages > 1:
                page_lines = file_lines[page_id * 20:(page_id + 1) * 20]
            else:
                page_lines = file_lines

            result = {
                'file_msg': ''.join(page_lines),
                'pages': pages,
                'page_id': page_id
            }
            self.set_result(result)
        except Exception, e:
            print e
            self.set_error(1, 'Read file error')
