#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import options, define, parse_command_line
from tornado_sqlalchemy import make_session_factory
from router import url_map
from src.utils import config
from env import set_env
set_env()


DB_HOST = config.get('mysql', 'host')
DB_PORT = config.get('mysql', 'port')
DB = config.get('mysql', 'database')
DB_USER = config.get('mysql', 'user')
DB_PWD = config.get('mysql', 'password')
mysql_engine = 'mysql+mysqldb://%s:%s@%s:%s/%s' % (DB_USER, DB_PWD, DB_HOST, DB_PORT, DB)

factory = make_session_factory(mysql_engine)
port = config.get('global', 'port')
debug_model = int(config.get('global', 'debug_model'))
process_num = int(config.get('global', 'process_num'))
define("port", default=port, help=" server listen port")

settings = {
    'debug': debug_model,
    'session_factory': factory,
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
