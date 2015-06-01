#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website
"""
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from handlers.index import IndexHandler
from handlers.index import ErrorHandler
from handlers.index import RegisterHandler
from handlers.user import UserHandler

url = [
    (r'/', IndexHandler),
    (r'/error', ErrorHandler),
    (r'/login', RegisterHandler),
    (r'/user', UserHandler),
]
