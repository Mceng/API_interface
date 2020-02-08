#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/2/4
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_login

import allure
import pytest
from base.get_params import GetParams
from utils.Request import Request
from utils.Assert import Assertions


@allure.feature('登陆注册退出模块')
class TestLogin():
    @allure.severity('登陆')
    @allure.story('登陆正向用例')
    @pytest.mark.skip('不执行登录用例')
    def test_pass(self,params_init):

        """
        用例描述：登陆正向用例

        """
        self.request = Request()
        self.params = params_init.get_params_list('login')
        self.test_assert = Assertions()

        response = self.request.post_request(self.params['Login'][0]['url'],\
                                             self.params['Login'][0]['data'], \
                                             self.params['Login'][0]['header'])
        print(response)


        assert self.test_assert.assert_code(response['code'], 200)
        assert self.test_assert.assert_body(response['body'], 'msg', 'OK')
