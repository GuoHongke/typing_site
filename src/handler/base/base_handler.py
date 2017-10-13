#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from tornado.web import RequestHandler
from tornado_sqlalchemy import SessionMixin
from src.utils.logger import logger


class BaseHandler(RequestHandler, SessionMixin):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

        self._status = 0
        self._error_message = None
        self._result = {}

        self.account_id = self.get_secure_cookie('account_id')

    def prepare(self):
        logger.api_logger().api_info('handler %s args %s' % (self.__class__.__name__, self.request.arguments))

    def head(self, *args, **kwargs):
        self.run()

    def get(self, *args, **kwargs):
        self.run()

    def post(self, *args, **kwargs):
        try:
            body = json.loads(self.request.body if self.request.body else '{}')
            for key, value in body.items():
                self.request.arguments[key] = [value]
        except Exception, e:
            logger.api_logger().api_error(e)
        self.run()

    def options(self, *args, **kwargs):
        self.run()

    def data_received(self, chunk):
        pass

    def run(self):
        with self.make_session() as session:
            self.do_action(session)
        self.do_response()

    def do_action(self, session):
        pass

    def do_response(self):
        response = {
            "status": self._status
        }
        if self._error_message:
            response["error_message"] = self._error_message
            logger.api_logger().api_error(self._error_message)
        response.update(self._result)

        if self.request.method == 'OPTIONS':
            self.set_header("Access-Control-Allow-Headers", "Content-Type")

        origin = self.request.headers.get('Origin', '*')
        self.set_header("Access-Control-Allow-Origin", origin)
        self.set_header('Access-Control-Allow-Credentials', 'true')
        self.set_header("Content-Type", "application/json;charset=utf-8")
        self.write(json.dumps(response))

    def set_result(self, result):
        self._result = result

    def set_error(self, error_code, error_message, result=None):
        if result is None:
            result = {}
        self._status = error_code
        self._error_message = error_message
        self._result = result
