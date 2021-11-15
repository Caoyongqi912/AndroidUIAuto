# -*- coding: utf-8 -*-

# @Time    : 2021/10/14 9:53 上午 
# @Author  : cyq
# @File    : common.py
import time

from utils.deviceOpt import DeviceOpt
from elements.baseEle import BaseElements as BE


class Common(DeviceOpt):
    """
    公共方法
    """

    def _favorite(self) -> None:
        """
        点击搜藏
        """

        self.click(**BE.BUTTON_FAVORITE)

    def _call(self) -> None:
        """
        现在通话
        """
        self.click(**BE.BUTTON_CALL)

    def _delete_user(self):
        """
        点击删除
        :return:
        """
        self.click(**BE.BUTTON_DELETE)

    def _add_contact(self, mobile: str, company: str):
        """
        添加外部联系人
        :param mobile: mobile
        :param company: company
        :return:
        """
        self.send(mobile, **BE.INPUT_CONTACT)
        self.click(**BE.DROP_CONTACT)
        self.click(**BE.CHOICE_COMPANY(company))
        self.click(**BE.BUTTON_SAVE)

    def verify_space(self, space: bool) -> bool:
        """
        判断所在空间
        :return: x if space is team else privacy
        """
        time.sleep(1)
        if space is True:
            return self.getEleAttr("checked", **SE.BUTTON_TEAM)
        else:
            return self.getEleAttr("checked", **SE.BUTTON_PRIVACY)

    def click_quite(self) -> None:
        """
        点击退出
        """
        self.click(**SE.BUTTON_QUIT)

    def logout(self) -> bytes:
        """
        退出登录
        :return: pic
        """

        self.click_setting()
        self.click_quite()
        time.sleep(1.5)
        return self.screenShot()

    def get_snackbar_text(self) -> str:
        """
        获取弹窗文案
        :return: str
        """

        return self.getText(**BE.SNACKBAR_TEXT)

    def search_back(self) -> None:
        """
        后退
        :return:
        """
        self.click(**BE.SEARCH_BACK)

    def verify_setting(self) -> bool:
        """
        设置界面
        :return bool
        """
        return self.exist(**BE.LAYOUT_SETTING)

    def get_setting_userInfo(self) -> str:
        """
        获取设置用户信息
        :return: info
        """
        return self.getText(**BE.TEXT_SETTING_USERINFO)

    def click_setting(self):
        """
        点击设定
        """
        self.click(**BE.BUTTON_SETTING)

