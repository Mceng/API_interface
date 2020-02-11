#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/2/4
# @Author  : Mcen (mmocheng@163.com)
# @Name    : conftest

import pytest
import allure
import requests
from utils.common import CommonUtil
from base.element_path import Element
from utils.Request import Request
from utils.log import MyLog
from utils.Assert import Assertions
from base.get_params import GetParams
from base import consts
from utils.data_cleanup import Data_Cleanup


@pytest.fixture(scope='session')
def common_init():
    return CommonUtil()


@pytest.fixture(scope='session')
def params_init():
    return GetParams()


@pytest.fixture(scope='session')
def request_init():
    return Request()


@pytest.fixture(scope='session')
def log():
    return MyLog()


@pytest.fixture(scope='session')
def assert_init():
    return Assertions()

@pytest.fixture(scope='session', autouse=True)
def session_init():
    """
    数据准备
    :return:
    """
    # allure.environment(测试环境="online", hostName="host", 执行人="XX", 测试项目="线上接口测试")

    # 1、实例化
    common = CommonUtil()

    # 1、cookie准备
    try:
        url = 'https://iparking.ibotech.com.cn/monitor3/auth_user/login'
        data = {"userName": "13800138001", "password": 138001, "captcha": "", "Code": "false", "rememberMe": "false"}
        r = requests.post(url=url, data=data)
        cookieid = requests.utils.dict_from_cookiejar(r.cookies)
        cookie = "sid=" + cookieid['sid']
        common.write_file(Element.COOKIE_FILE, cookie)
        print(cookie)
    except:
        print('生成cookie失败')
    else:
        print('生成cookie成功')

    yield
    # 后置操作
    # Data_Cleanup.data_cleanup()
    print(consts.TIMES_LIST)
