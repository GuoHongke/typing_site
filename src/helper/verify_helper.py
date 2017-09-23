#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


class VerifyHelper(object):
    @staticmethod
    def pwd_len_check(pwd):
        if len(pwd) > 24 or len(pwd) < 8:
            return False
        else:
            return True

    @staticmethod
    def pwd_space_check(pwd):
        pattern_space = re.compile(r'\s+')
        match = pattern_space.findall(pwd)
        if match:
            return False
        else:
            return True

    @staticmethod
    def pwd_safety_check(pwd):
        # 密码至少包含(字母/数字/特殊符号)中的两种
        pattern = re.compile(r'(?!^(\d+|[a-zA-Z]+|[^a-z0-9A-Z]+)$)^.+$')
        match = pattern.findall(pwd)
        if match:
            return False
        else:
            return True

    @staticmethod
    def mail_check(mail):
        if re.match("[^\._-][\w\.]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+$", mail):
            return True
        else:
            return False

    @staticmethod
    def name_check(name):
        # 不以下划线开头，仅包含字母、数字或下划线的用户名
        if re.match(r'^(?!_)[a-zA-Z0-9_\u4e00-\u9fa5]+$'):
            return True
        else:
            return False

    def password_verify(self, pwd):
        error_msg = None
        if not self.pwd_len_check(pwd):
            error_msg = u'请输入长度为8-24位的密码'
        elif not self.pwd_space_check(pwd):
            error_msg = u'密码中不能包含空格'
        elif not self.pwd_safety_check(pwd):
            error_msg = u'密码至少包含(字母/数字/特殊符号)中的两种'
        return error_msg


