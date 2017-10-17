#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, VARCHAR, DATETIME, TEXT
from . import Base


class Lessons(Base):
    __tablename__ = 'lessons'

    id = Column(String(255), primary_key=True)
    name = Column(String(255), nullable=False)
    account_id = Column(String(255), nullable=False)
    file_id = Column(VARCHAR(255), nullable=False)
    create_time = Column(DATETIME, nullable=False)
    notes = Column(TEXT, nullable=False)

    def __repr__(self):
        return "<Lesson(id='%s', name='%s', account_id=%s, file_id=%s, notes=%s)>" % \
               (self.id, self.name, self.account_id, self.file_id, self.notes)
