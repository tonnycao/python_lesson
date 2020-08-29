# -*- coding: utf-8 -*-
# @Time : 2020/8/29 3:58 下午
# @Author : tonnycao
# @Email : wayne_lau@aliyun.com
# @File : forms.py
# @Project : flasker

import os


DEBUG = False
TESTING = False
CSRF_ENABLED = True
CSRF_SESSION_KEY = "secret"
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SECRET_KEY = b'\x83y\x0e\x93\xe8\x8e\xcc\xe0\xbdnH\x861\x98\x08\xd7'