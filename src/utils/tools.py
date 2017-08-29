#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid


def unique_id(prefix=None):
    u_id = str(uuid.uuid4()).replace("-", "")

    return u_id if not prefix else "%s_%s" % (prefix, u_id)
