#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/2/4
# @Author  : Mcen (mmocheng@163.com)
# @Name    : config


from configparser import ConfigParser
from base.element_path import Element


class Config:

    def __init__(self):
        self.config = ConfigParser()
        self.conf_path = Element.CONFIG

        self.config.read(self.conf_path, encoding='utf-8')

        # base_url
        self.base_url = self.get_conf('base_url', 'url')

        # private_debug测试服务
        self.debug_base_url = self.get_conf('private_debug', 'base_url')
        self.debug_tester = self.get_conf('private_debug', 'tester')
        self.debug_environment = self.get_conf('private_debug', 'env')
        self.debug_versionCode = self.get_conf('private_debug', 'versionCode')
        self.debug_loginHost = self.get_conf('private_debug', 'loginHost')
        self.debug_loginInfo = self.get_conf('private_debug', 'loginInfo')

        # online_release测试服务
        self.release_base_url = self.get_conf('online_release', 'base_url')
        self.release_tester = self.get_conf('online_release', 'tester')
        self.release_environment = self.get_conf('online_release', 'env')
        self.release_versionCode = self.get_conf('online_release', 'versionCode')
        self.release_loginHost = self.get_conf('online_release', 'loginHost')
        self.release_loginInfo = self.get_conf('online_release', 'loginInfo')



        # 头部
        self.header1 = self.get_conf('header','header1')
        self.header2 = self.get_conf('header','header2')

        # 数据库
        self.mysql_host = self.get_conf('mysql', 'host')
        self.mysql_port = self.get_conf('mysql', 'port')
        self.mysql_user = self.get_conf('mysql', 'user')
        self.mysql_password = self.get_conf('mysql', 'password')
        self.mysql_db = self.get_conf('mysql', 'db')
        self.mysql_charset = self.get_conf('mysql', 'charset')

        # 邮箱
        self.mail_smtpserver = self.get_conf('mail', 'smtpserver')
        self.mail_sender = self.get_conf('mail', 'sender')
        self.mail_receiver = self.get_conf('mail', 'receiver')
        self.mail_name = self.get_conf('mail', 'name')
        self.mail_username = self.get_conf('mail', 'username')
        self.mail_password = self.get_conf('mail', 'password')

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def get_env(self,env):
        if env == 'debug':
            env = {
                'base_url':self.debug_base_url,
                'tester':self.debug_tester,
                'environment':self.debug_environment,
                'versionCode':self.debug_versionCode,
                'loginHost':self.debug_loginHost,
                'loginInfo':self.debug_loginInfo
            }

        elif env == 'release':
            env = {
                'base_url': self.release_base_url,
                'tester': self.release_tester,
                'environment': self.release_environment,
                'versionCode': self.release_versionCode,
                'loginHost': self.release_loginHost,
                'loginInfo': self.release_loginInfo
            }
        else:env=()
        return env


if __name__ == '__main__':
    a = Config()
    print(a.debug_base_url)
