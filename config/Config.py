# -*- coding: utf-8 -*-

# @Time    : 2021/8/12 4:18 下午 
# @Author  : cyq
# @File    : Config.py
import os
from configparser import ConfigParser
from utils.log import log
from typing import Union


class Config:
    # path
    path = os.path.dirname(os.path.dirname(__file__))

    def __init__(self):
        self.xml_report_path = Config.path + '/report/DispatchXml'
        self.html_report_path = Config.path + '/report/DispatchHtml'
        self.pic_path = Config.path + '/report/Pic'

        self.config = ConfigParser()
        self.config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')

        if not os.path.exists(self.config_path):
            raise FileNotFoundError('配置文件不存在！')
        self.config.read(self.config_path)

    def get_conf(self, title: str, value: str) -> Union[list, str]:
        """
        read .ini
        :param title:
        :param value:
        :return:
        """
        _v = self.config.get(title, value)
        if value == "ip":
            _v = _v.split(",")
        log.info(f"{title, value} -> {_v}")

        return _v

    def set_conf(self, title: str, value: str, text: str) -> None:
        """
        change .ini
        :param title:
        :param value:
        :param text:
        :return:
        """

        log.info("{} : {}:{}:{}".format(self.set_conf.__name__, title, value, text))

        self.config.set(title, value, text)
        with open(self.config_path, 'w+') as f:
            return self.config.write(f)

    def add_conf(self, title: str) -> None:
        """
        add .ini
        :param title:
        :return:
        """

        log.info("{} : {}".format(self.add_conf.__name__, title))

        self.config.add_section(title)
        with open(self.config_path, 'w+') as f:
            return self.config.write(f)

    def get_user(self, username: str):

        info = {
            "mobile": self.config.get(username, "mobile"),
            "company": self.config.get(username, "company"),
            "code": self.config.get(username, "code"),
            "space": bool(self.config.get(username, "space")),
        }

        log.info(f"{info}")
        return info

    def get_version(self) -> str:
        """
        获取版本
        :return:
        """
        v = self.config.get("application", "package_url").split("-")[-2]
        log.info(v)
        return v


config = Config()

if __name__ == '__main__':
    config.get_version()
