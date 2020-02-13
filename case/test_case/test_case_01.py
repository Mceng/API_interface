#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/2/6
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_01

import pytest
import allure
from base import consts


# @allure.feature # 用于定义被测试的功能，被测产品的需求点
# @allure.story # 用于定义被测功能的用户场景，即子功能点
# with allure.step # 用于将一个测试用例，分成几个步骤在报告中输出
# allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
# @pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤

@allure.feature('测试模块')
class TestCase:

    @allure.story('get用例1')
    def test_case_get1(self, assert_init, params_init, request_init):
        """
        get获取数据，带参数
        """
        self.params = params_init.get_params_list('test_case')
        url = self.params['get_case'][0]['url']
        data = self.params['get_case'][0]['data']
        header = self.params['get_case'][0]['header']

        response = request_init.get_request(url=url, data=data, header=header)
        count = params_init.get_db_data('Project_count')['count']

        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'count', count)
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')

    @allure.story('get2不带参数用例')
    @allure.severity('blocker')
    @allure.issue("http://www.baidu.com")
    @allure.testcase("http://www.tgkkk.com")
    def test_case_get2(self, assert_init, params_init, request_init):
        """
        get获取数据不带参数
        """
        self.params = params_init.get_params_list('test_case')
        url = self.params['get_case'][0]['url']
        header = self.params['get_case'][0]['header']

        response = request_init.get_request(url=url, data=None, header=header)

        count = params_init.get_db_data('Project_count')['count']

        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'count', count)
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')

    @allure.story('post用例')
    def test_case_post1(self, assert_init, params_init, request_init):
        """
        post获取数据，带参数
        """

        self.params = params_init.get_params_list('test_case')
        url = self.params['post_case'][0]['url']
        header = self.params['post_case'][0]['header']
        data = self.params['post_case'][0]['data']
        with allure.step("步骤1"):
            allure.attach(url, header,data)
        with allure.step("校验结果"):
            allure.attach('期望结果', '成功')

        response = request_init.post_request(url=url, data=None,json=data, header=header)
        assert assert_init.assert_code(response['code'], 400)
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')


    @allure.story('put用例')
    def test_case_put(self,params_init,assert_init,request_init):
        self.params = params_init.get_params_list('test_case')
        url = self.params['put_case'][0]['url']
        header = self.params['put_case'][0]['header']
        data = self.params['put_case'][0]['data']
        response = request_init.put_request(url=url,json=data,data=None,header=header)

        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')




