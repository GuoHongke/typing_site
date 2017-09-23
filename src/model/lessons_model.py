#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, VARCHAR, TEXT
from . import Base


class Lessons(Base):
    __tablename__ = 'lessons'

    id = Column(String(255), primary_key=True)
    name = Column(String(255), nullable=False)
    account_id = Column(String(255), nullable=False)
    file_id = Column(VARCHAR(255), nullable=False)
    history_msg = Column(TEXT, nullable=True)

    def __repr__(self):
        return "<Lesson(id='%s', name='%s')>" % (self.id, self.name)
