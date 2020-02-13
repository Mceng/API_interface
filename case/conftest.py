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
from base.oper_token import OperToken
from utils.Request import Request
from utils.log import MyLog
from utils.Assert import Assertions
from base.get_params import GetParams
from base import consts
from utils.data_cleanup import Data_Cleanup


def evn():
    return consts.API_ENV_DEBUG

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
    env = consts.API_ENV_DEBUG


    # 1、cookie准备
    OperToken().generate_cookie(env)

    yield
    # 后置操作
    # Data_Cleanup.data_cleanup()
    print(consts.TIMES_LIST)
