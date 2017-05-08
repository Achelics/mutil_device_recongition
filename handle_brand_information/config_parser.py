#!/usr/bin/env/ python
# coding=utf-8
__author__ = ''
__Date__ = ''


import os as _os

from ConfigParser import *


class Config(object):
    """
    """
    def __init__(self, config_file, section):
        """Config 类的构造函数

        :param config_file: name of config file
        :type config_file: string

        :param section: name of section
        :type section: string
        """

        self.file_name = config_file
        self.section = section

        self.cf = ConfigParser()

        self._is_valid = True

        self._config_options = self._read_config()

    def _read_config(self):
        """读取配置文件

        :return: options of section
        :rtype: list
        """
        # check if config file exists
        if _os.path.exists(self.file_name):
            # check synatx of config file
            try:
                self.cf.read(self.file_name)

            # config file contains no section headers
            except MissingSectionHeaderError as msg:
                print("{0}".format(msg))
                self._is_valid = False
                return []

        # config file not exists
        else:
            print("找不到配置文件 {0}".format(self.file_name))
            self._is_valid = False
            return []
        # check if there are sections in config file
        try:
            config_options = self.cf.items(self.section)
            return config_options
        except NoSectionError as msg:
            print('{0}'.format(msg))
            self._is_valid = False
            return []

    def _get(self, option):
        """获取指定配置参数的值，返回字符串

        :param option: name of option
        :type option: string

        :return: value of option
        :rtype: string or None
        """
        # check if option exists
        try:
            value = self.cf.get(self.section, option)
        except NoOptionError as msg:
            print('{0}'.format(msg))
            value = None

        return value

    def get(self, option):
        """获取指定配置参数的值，如果正确则返回字符串，如果为None 则退出

        :param option: name of option
        :type option: string

        :return: value of option
        :rtype: string or None
        """
        value = self._get(option)
        if value is None:
            exit()
        else:
            return value

    def getint(self, option):
        """获取指定配置参数的值，返回整数

        :param option: name of option
        :type option: string

        :return: value of option
        :rtype: int
        """
        # check if option exsits

        value = self._get(option)
        if value is None:
            exit()
        else:
            # check value type
            try:
                value = int(value)
            except ValueError as msg:
                print("参数无效 '{0}'--{1}".format(option,msg))
                exit()
        return value

    def has_option(self, option):
        """检查配置文件中是否包含某个项

        :param option:
        :type option: str
        :return: True if option exists,otherwise False
        """
        return self.cf.has_option(self.section, option)

    @property
    def isvalid(self):
        """配置文件是否可用

        :return: True if config is valid, otherwise False
        :rtype: boolean
        """

        return self._is_valid

    @property
    def opt(self):
        """配置文件中所有配置参数

        :return: list of options
        :rtype: list
        """

        return self._config_options