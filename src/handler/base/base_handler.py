#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import time
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

        self._error_message = ""
        self._result = {}

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
            "status": self.get_status(),
            "error_message": self._error_message,
        }

        response.update(self._result)

        self.set_header("Content-Type", "application/json;charset=utf-8")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(json.dumps(response))

    def set_result(self, result):
        self._result = result

    def set_error(self, error_message, result=None):
        if result is None:
            result = {}
        self._error_message = error_message
        self._result = result