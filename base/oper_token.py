#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/4/24
# @Author  : Mcen (mmocheng@163.com)
# @Name    : oper_token


import logging,requests
from base.element_path import Element
from utils.common import CommonUtil

class OperToken:
    def __init__(self):
        self.common = CommonUtil()

    def write_cookie(self):
        logging.info('初始化用例，获取cookie')
        url = 'https://iparking.ibotech.com.cn/monitor3/auth_user/login'
        data = {"userName": "13800138001",
                "password": 138001,
                "captcha": "",
                "Code": "false",
                "rememberMe": "false"
                }
        r = requests.post(url=url, data=data)
        cookieid = requests.utils.dict_from_cookiejar(r.cookies)
        cookie = "sid=" + cookieid['sid']
        self.common.write_file(Element.COOKIE_FILE, cookie)
        print(cookie)
        logging.info('结束始化用例，已获取到cookie')

    def get_cookie(self):
        return self.common.read_file(Element.COOKIE_FILE)

if __name__ == '__main__':
    o = OperToken()
    o.write_cookie()