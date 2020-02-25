#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/2/17
# @Author  : Mcen (mmocheng@163.com)
# @Name    : mock

from unittest import mock
import logging


def mock_test(mock_method,request_data,url,method,response_data):
    logging.info('mock数据')
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url,method,request_data)
    return res
