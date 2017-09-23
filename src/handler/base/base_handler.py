#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import time
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

        self._status = 0
        self._error_message = None
        self._result = {}

        self.account_id = self.get_secure_cookie('account_id')

    def head(self, *args, **kwargs):
        self.do_action()
        self.do_response()

    def get(self, *args, **kwargs):
        self.do_action()
        self.do_response()

    def post(self, *args, **kwargs):
        self.do_action()
        self.do_response()

    def options(self, *args, **kwargs):
        self.do_action()
        self.do_response()

    def data_received(self, chunk):
        pass

    def do_action(self):
        pass

    def do_response(self):
        response = {
            "status": self._status
        }
        if self._error_message:
            response["error_message"] = self._error_message

        response.update(self._result)

        self.set_header("Content-Type", "application/json;charset=utf-8")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(json.dumps(response))

    def set_result(self, result):
        self._result = result

    def set_error(self, error_code, error_message, result=None):
        if result is None:
            result = {}
        self._status = error_code
        self._error_message = error_message
        self._result = result
