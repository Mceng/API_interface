#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/4/24
# @Author  : Mcen (mmocheng@163.com)
# @Name    : oper_token


import logging,requests
from base.element_path import Element
from utils.common import CommonUtil
from config.config import Config

class OperToken:
    def __init__(self):
        self.common = CommonUtil()

    def generate_cookie(self,env):

        if env == 'debug':
            logging.info('初始化用例，获取cookie')
            url = Config().debug_base_url + Config().debug_loginHost
            data = eval(Config().debug_loginInfo)
            r = requests.post(url=url, data=data)
            cookieid = requests.utils.dict_from_cookiejar(r.cookies)
            cookie = "sid=" + cookieid['sid']
            self.common.write_file(Element.COOKIE_FILE, cookie)
            print(cookie)
            logging.info('结束始化用例，已获取到cookie')
        elif env == 'release':
            pass
        else:
            print('环境错误')

    def get_cookie(self):
        return self.common.read_file(Element.COOKIE_FILE)

if __name__ == '__main__':
    o = OperToken()
    o.generate_cookie('debug')