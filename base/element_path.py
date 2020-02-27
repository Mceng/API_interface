#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/2/4
# @Author  : Mcen (mmocheng@163.com)
# @Name    : element_path

"""
定义文件路径
"""

import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Element():
    COOKIE_FILE = PATH("../params/cookie")
    CLEANUP_DATA = PATH("../params/cleanup_sql.yml")
    REPORT_XML = PATH("../reports/xml")
    REPORT_HTML = PATH("../reports/html")
    CONFIG = PATH("../config/config.ini")
    PARAMS = PATH("../params/api_yml")
    ASSERT_SQL = PATH("../params/assert_sql.yml")
    Allure_Path = PATH("../reports/allure-2.12.1/bin")
    ENVIRONMENT = PATH("../reports/xml/environment.xml")
