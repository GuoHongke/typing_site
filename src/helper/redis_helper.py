#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
from src.utils import config


class RedisClient(object):
    def __init__(self):
        self.host = config.get('redis', 'host')
        self.port = config.get('redis', 'port')
        self.db = config.get('redis', 'db')

    def connect(self):
        redis_client = redis.Redis(host=self.host, port=self.port, db=self.db)
        return redis_client

