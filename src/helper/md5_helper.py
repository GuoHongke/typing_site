#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from hashlib import md5
from random import randint


class Md5Helper(object):
    """
        Md5 key generator helper
        key_gen: make unique id
        ori_str_gen: for encoding the password
        access_token: for token of connect
    """

    @staticmethod
    def key_gen(ori_str):
        """生成key"""
        return "%s" % (md5(ori_str).hexdigest()[8:-8] + md5("%s_%s_%s" % (ori_str, time.time(),
                                                                          randint(0, 100000))).hexdigest())

    @staticmethod
    def ori_str_gen(ori_str):
        """生成key"""
        return md5(md5(ori_str).hexdigest()).hexdigest()