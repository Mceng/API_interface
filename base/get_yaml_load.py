#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/2/20
# @Author  : Mcen (mmocheng@163.com)
# @Name    : get_yaml_load
import os,re
import aiofiles
import yaml


async def yaml_load(dir='', file=''):
    """
    异步读取yaml文件，并转义其中的特殊值
    :param file:
    :return:
    """
    if dir:
        file = os.path.join(dir, file)
    async with aiofiles.open(file, 'r', encoding='utf-8', errors='ignore') as f:
        data = await f.read()

    data = yaml.load(data)

    # 匹配函数调用形式的语法
    pattern_function = re.compile(r'^\${([A-Za-z_]+\w*\(.*\))}$')
    pattern_function2 = re.compile(r'^\${(.*)}$')
    # 匹配取默认值的语法
    pattern_function3 = re.compile(r'^\$\((.*)\)$')

    def my_iter(data):
        """
        递归测试用例，根据不同数据类型做相应处理，将模板语法转化为正常值
        :param data:
        :return:
        """
        if isinstance(data, (list, tuple)):
            for index, _data in enumerate(data):
                data[index] = my_iter(_data) or _data
        elif isinstance(data, dict):
            for k, v in data.items():
                data[k] = my_iter(v) or v
        elif isinstance(data, (str, bytes)):
            m = pattern_function.match(data)
            if not m:
                m = pattern_function2.match(data)
            if m:
                return eval(m.group(1))
            if not m:
                m = pattern_function3.match(data)
            if m:
                K, k = m.group(1).split(':')
                return bxmat.default_values.get(K).get(k)

            return data

    my_iter(data)

    return BXMDict(data)