#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, INT, String, TEXT
from . import Base


class History(Base):
    __tablename__ = 'history'

    id = Column
    lesson_id = Column(INT, primary_key=True, autoincrement=True)
    account_id = Column(String(255), nullable=False)
    history_msg = Column(TEXT, nullable=True)

    def __repr__(self):
        return "<History(account_id='%s', lesson_id='%s')>" % (self.account_id, self.lesson_id)
