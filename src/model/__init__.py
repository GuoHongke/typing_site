#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.utils import config

DB_HOST = config.get('mysql', 'host')
DB_PORT = config.get('mysql', 'port')
DB = config.get('mysql', 'database')
DB_USER = config.get('mysql', 'user')
DB_PWD = config.get('mysql', 'password')
mysql_engine = 'mysql+mysqldb://%s:%s@%s:%s/%s' % (DB_USER, DB_PWD, DB_HOST, DB_PORT, DB)

Base = declarative_base()

engine = create_engine(mysql_engine)
DBSession = sessionmaker(bind=engine)
