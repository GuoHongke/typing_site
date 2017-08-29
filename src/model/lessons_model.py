#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String
from . import Base


class Files(Base):
    __tablename__ = 'lessons'

    id = Column(String(255), primary_key=True)
    file_id = Column(String(255), nullable=False)

    def __repr__(self):
        return "<Lesson(id='%s', file_id='%s')>" % (self.id, self.file_id)
