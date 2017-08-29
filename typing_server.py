#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import options, define, parse_command_line
from router import url_map
from src.utils import config
from env import set_env
set_env()

port = config.get('global', 'port')
define("port", default=port, help=" server listen port")


def main():
    parse_command_line()
    app = tornado.web.Application(url_map)
    server = tornado.httpserver.HTTPServer(app, max_body_size=800 * 1024 * 1024)
    server.bind(options.port)
    server.start()
    print 'Server start on port %s' % options.port
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
