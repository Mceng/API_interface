#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/2/4
# @Author  : Mcen (mmocheng@163.com)
# @Name    : run


"""
运行用例集：
    python3 run.py

# '--allure_severities=critical, blocker'
# '--allure_stories=测试模块_demo1, 测试模块_demo2'
# '--allure_features=测试features'

"""
import sys

import pytest

from utils.shell import Shell
from utils import log
from base.element_path import Element
from utils.send_email import SendMail

if __name__ == '__main__':
    log = log.MyLog()
    # log.info('初始化配置文件')
    # log.error('执行用例失败，请检查环境配置')

    xml_report_path = Element.REPORT_XML
    html_report_path = Element.REPORT_HTML

    # 定义测试集
    # args = ['-s', '-q', '--alluredir', xml_report_path]
    # pytest.main(args)

    pytest.main()
    cmd = 'allure generate %s -o %s' % (xml_report_path, html_report_path)

    try:
        Shell.run_shell(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise


    # 发送邮件
    # SendMail().send_mail()


