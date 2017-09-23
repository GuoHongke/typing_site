#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, TEXT
from . import Base


class Account(Base):
    __tablename__ = 'account'

    id = Column(String(255), primary_key=True)
    name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    lessons = Column(TEXT, nullable=True)

    def __repr__(self):
        return "<Account(id='%s', name='%s')>" % (self.id, self.name)

