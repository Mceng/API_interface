#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/2/4
# @Author  : Mcen (mmocheng@163.com)
# @Name    : get_params

"""
读取yaml测试数据

"""

from utils.common import CommonUtil
from config.config import Config
from base.oper_token import OperToken
from utils.operation_db import Opera_DB

class GetParams:
    def __init__(self):
        self.common= CommonUtil()
        self.cookie = OperToken().get_cookie()
        self.db = Opera_DB()

    def get_params_list(self,file_name):
        self.params = self.common.read_params(file_name)
        _page_list = {}
        for page, value in self.params.items():
            parameters = value['parameters']
            data_list = []

            for parameter in parameters:
                parameter['url'] = Config().base_url + parameter['url']
                # parameter['header']['Cookie'] = self.cookie
                data_list.append(parameter)
            _page_list[page] = data_list
        return _page_list

    def get_db_data(self,key,way='one'):
        """
        通过关键字获取对应的sql执行后返回的数据
        :param key: 关键字
        :param way: 定义返回多少条数据，one一条，all是所有
        :return:
        """
        return self.db.select_data(self.common.get_sql(key),way)



if __name__ == '__main__':
    lists = GetParams()
    print(lists.get_db_data('Project_count'))
    print(lists.get_db_data('Login'))
