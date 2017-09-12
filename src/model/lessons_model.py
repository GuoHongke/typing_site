#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, VARCHAR
from . import Base


class Lessons(Base):
    __tablename__ = 'lessons'

    id = Column(String(255), primary_key=True)
    name = Column(String(255), nullable=False)
    file_ids = Column(VARCHAR(255), nullable=False)

    def __repr__(self):
        return "<Lesson(id='%s', file_ids='%s')>" % (self.id, self.file_ids)
