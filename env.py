#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


reload(sys)
sys.setdefaultencoding('utf-8')


def set_env():
    cur_dir = sys.path[0]
    os.sys.path.append(os.path.join(cur_dir, "src"))

    os.environ["CONF"] = os.path.join(cur_dir, "conf")
    os.environ["SRC"] = os.path.join(cur_dir, "src")
    os.environ["TEMPLATES"] = os.path.join(cur_dir, "templates")
    os.environ["STATIC"] = os.path.join(cur_dir, "static")