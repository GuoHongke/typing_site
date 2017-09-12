#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String
from . import Base


class Files(Base):
    __tablename__ = 'files'

    id = Column(String(255), primary_key=True)
    name = Column(String(255), nullable=False)
    plang = Column(String(255), nullable=False)

    def __repr__(self):
        return "<File(id='%s', name='%s')>" % (self.id, self.name)

