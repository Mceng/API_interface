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
        self.base_url = Config().base_url

    def get_params_list(self,file_name):
        self.params = self.common.read_params(file_name)
        _page_list = {}
        for page, value in self.params.items():
            parameters = value['parameters']
            data_list = []
            for parameter in parameters:
                parameter['url'] = self.base_url + parameter['url']
                # parameter['header']=self.operate_header(parameter['header'])
                data_list.append(parameter)
            _page_list[page] = data_list
        return _page_list

    def operate_header(self,key):
        """
        重新处理头部
        :param key:
        :return:
        """
        if key is None:
            header = {}
        elif key == 'header1':
            header =  Config().header1
        elif key == 'header2':
            header = Config().header2
        else:
            return '头部处理错误'
        header['Cookie'] = self.cookie
        return header

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
    print(lists.get_params_list('test_case'))
    # print(lists.get_db_data('Login'))
