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
debug_model = int(config.get('global', 'debug_model'))
process_num = int(config.get('global', 'process_num'))
define("port", default=port, help=" server listen port")
settings = {
    'debug': debug_model,
    'cookie_secret': 'L8LwECiNRxq2N0N2eGxx9MZlrpmuMEimlydNX/vt1LM='
}


def main():
    parse_command_line()
    app = tornado.web.Application(url_map, **settings)
    server = tornado.httpserver.HTTPServer(app, max_body_size=800 * 1024 * 1024)
    server.bind(options.port)
    server.start(1 if debug_model else process_num)
    print 'Server start on port %s' % options.port
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
