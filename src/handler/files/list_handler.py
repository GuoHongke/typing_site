#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.handler.base.base_handler import BaseHandler
from src.model.files_model import Files
from src.utils.logger import logger


class FileListHandler(BaseHandler):
    def do_action(self, session):
        try:
            files = session.query(Files.id, Files.name).filter(Files.account_id == self.account_id)
            file_list = []
            for f in files:
                _file = {
                    'name': f.name,
                    'file_id': f.file_id,
                }
                file_list.append(_file)

            self.set_result({
                'file_list': file_list
            })
        except Exception, e:
            logger.api_logger().api_error(e)
            self.set_error(1, u'服务器内部错误')
