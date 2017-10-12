#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.handler.account.login_handler import LoginHandler
from src.handler.account.logout_handler import LogoutHandler
from src.handler.account.register_handler import RegisterHandler
from src.handler.account.show_handler import ShowHandler
from src.handler.account.update_handler import UpdateHandler
from src.handler.lessons.home_handler import HomeHandler
from src.handler.lessons.list_handler import LessonListHandler
from src.handler.lessons.create_handler import LessonCreateHandler
from src.handler.lessons.save_handler import LessonSaveHandler
from src.handler.lessons.delete_handler import LessonDeleteHandler
from src.handler.lessons.history_handler import HistoryHandler
from src.handler.files.upload_handler import FileUploadHandler
from src.handler.files.delete_handler import FileDeleteHandler
from src.handler.files.list_handler import FileListHandler
from src.handler.files.get_handler import GetHandler


url_map = [
    (r'/account/login', LoginHandler),
    (r'/account/logout', LogoutHandler),
    (r'/account/register', RegisterHandler),
    (r'/account/show', ShowHandler),
    (r'/account/update', UpdateHandler),
    (r'/', HomeHandler),
    (r'/lesson/list', LessonListHandler),
    (r'/lesson/create', LessonCreateHandler),
    (r'/lesson/delete', LessonDeleteHandler),
    (r'/lesson/save', LessonSaveHandler),
    (r'/lesson/history', HistoryHandler),
    (r'/file', GetHandler),
    (r'/file/upload', FileUploadHandler),
    (r'/file/list', FileListHandler),
    (r'/file/delete', FileDeleteHandler)
]
