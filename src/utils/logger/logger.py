#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
import logging.config
from src.utils import config


LOG_DIR = config.get('global', 'log_dir')
LOG_CONF_PATH = os.path.join(os.getenv('CONF'), 'logging.conf')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.config.fileConfig(LOG_CONF_PATH, defaults={'log_dir': LOG_DIR})


class __Logger(object):
    def __init__(self, logger):
        self.logger = logger

    def api_info(self, message):
        self.logger.info(message)

    def api_debug(self, message):
        self.logger.debug(message)

    def api_warn(self, message):
        self.logger.warn(message)

    def api_error(self, message):
        self.logger.error(message)

    def api_critical(self, message):
        self.logger.critical(message)

__logger_map = {}


def __get_logger(name):
    if name in __logger_map:
        return __logger_map[name]
    else:
        logger = __Logger(logging.getLogger(name))
        __logger_map[name] = logger

        return logger


def api_logger():
    return __get_logger('api')