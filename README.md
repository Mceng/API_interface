# API_interface
这是一个基于pytest+request+allure 接口自动化 的项目

###模块类的设计 

项目结构：说明

            .
            |-- base                      ---------------------基础类
            |   |   |-- consts.py         --------------------- 全局变量
            |   |   |-- __init__.py
            |-- case                      --------------------- 测试用例模块
            |   |-- conftest.py
            |   |-- __init__.py
            |   |-- test_login            --------------------- 登录测试模块
            |   |   |-- conftest.py
            |   |   |-- __init__.py
            |   |   `-- test_login.py
            |-- logs                      --------------------- 输出日志
            |-- reports                   --------------------- 报告
            |-- params                    ---------------------- 测试数据
            |   |-- api_yml               --------------------- 接口数据
            |   -- assert_sql             ---------------------请求数据sql
            |   -- cleanup_sql            --------------------- 清理数据sql
            
            |-- utils                     ---------------------- 工具方法
            |-- README.md
            |-- pytest.ini                ---------------------- 配置文件
            |-- run.py                    ---------------------- 程序执行入口
