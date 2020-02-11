#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/5/26
# @Author  : Mcen (mmocheng@163.com)
# @Name    : test_03

import pytest

def setup_function():
    print("setup_function ：每个用例开始前都会执行")

def teardown_function():
    print( "teardown_function ：每个用例结束后都会执行")

def test_post():
    print("正在执行 ---- test_case_---test_one")
    x  =  "this"

    assert 'h' in x
    print("=========================================================")

def check_one():
    print("正在执行 ----check_one--- test_two")
    try:
        2>9
    except:
        raise
    x = "this"
    assert hasattr(x, 'check')

    print("=========================================================")

if __name__ == '__main__':
    pytest.main(['-s','test_031.py'])