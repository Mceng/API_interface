#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/8/10
# @Author  : Mcen (mmocheng@163.com)
# @Name    : data_cleanup
"""
封装数据清理
"""

from utils.operation_db import Opera_DB
from base.element_path import Element
from utils.common import CommonUtil
import logging

class Data_Cleanup:
    @staticmethod
    def data_cleanup():
        common = CommonUtil()
        data = common.read_yaml(Element.CLEANUP_DATA)
        print(data)
        # 读取出来后循环执行sql
        for key,values in data.items():
            logging.info('==执行( {} )的数据清理开始=='.format(data[key]['dec']))
            for i,sql in values.items():
                if i != 'dec':
                    logging.info('==执行sql=={}'.format(sql))
                    # 判断执行影响的行数
                    row = Opera_DB().commit_data(sql)
                    if row > 0:
                        logging.info('清理数据条数为：{}，清理成功！'.format(row))
            logging.info('==结束( {} )的数据清理=='.format(data[key]['dec']))

if __name__ == '__main__':
    Data_Cleanup.data_cleanup()



