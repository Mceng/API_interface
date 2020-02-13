#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/2/5
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_map


import allure
import pytest
from base import consts


@allure.feature('大屏数据')
class Test_MapIndex():

    @allure.story('基本信息')
    # @pytest.mark.usefixture("common_init")
    def test1_totalOverview_pass(self,common_init,request_init,assert_init,params_init):

        """
        用例描述：安全运行天数、历史警告次数、监测点总数、设备完好率
        """
        self.params = params_init.get_params_list('mapIndex')

        response = request_init.post_request(url=self.params['MapIndex'][0]['url'],data=None,json=self.params['MapIndex'][0]['data'],headers=self.params['MapIndex'][0]['header'])
        # print(response)
        # print(common_init.read_assert_sql())
        # print(init_data)



        assert assert_init.assert_code(response['code'], 200)
        assert assert_init.assert_body(response['body'], 'msg', 'OK')
        assert assert_init.assert_time(response['time_consuming'], 1100)
        consts.RESULT_LIST.append('True')
