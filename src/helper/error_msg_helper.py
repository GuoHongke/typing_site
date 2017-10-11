#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Error(object):
    # account error
    # login
    NO_LOGIN_CARD = "请输入登录名"
    NO_PASSWORD = "请输入密码"
    LOGIN_ERROR = "登录名或密码错误"
    # register/update
    NO_REGISTER_ARGS = "请输入完整注册信息"
    DUPLICATE_NAME = "用户名已被注册"
    DUPLICATE_MAIL = "邮箱已被注册"
    NAME_ERROR = "无效的用户名"
    MAIL_ERROR = "无效的邮箱"
    PWD_SPACE_ERROR = "密码不能有空白符"
    PWD_LEN_ERROR = "密码必须在8~18位之间"
    PWD_SAFETY_ERROR = "密码至少包含(字母/数字/特殊符号)中的两种"
    OLD_PWD_ERROR = "旧密码错误"
    NEW_PWD_ERROR = "新密码与旧密码相同"

    # file
    READ_ERROR = "文件读取失败"

    # lesson
    NO_LESSON_NAME = '课程名不能为空'
    LESSON_NO_FILE = '请为课程添加文件'
    DUPLICATE_LESSON = '课程名已存在'
    NO_FILE = '所选文件不存在'
    NO_LESSON = '课程不存在'
    NO_LESSON_ID = '请输入课程id'

    # global error
    NOT_LOGIN_ERROR = "请先登录"
    SERVER_ERROR = "服务器内部错误"