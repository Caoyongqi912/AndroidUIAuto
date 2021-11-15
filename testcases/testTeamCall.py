# -*- coding: utf-8 -*-

# @Time    : 2021/11/1 6:29 下午 
# @Author  : cyq
# @File    : testTeamCall.py
import allure
import pytest

from config.Config import config
from pages.teamPage import TeamPage
from utils.assertOpt import Assert
from utils.devicePool import DevicePool
from utils.u import U2


@allure.feature("通话")
class TestTeamCall:

    def setup_class(self):
        self.package = config.get_conf("application", "package_name")
        self.userInfo = config.get_user("userA")
        self.targetUserInfo = config.get_user("userB")
        self.targetUserName = config.get_conf("userB", "name")
        self.pool = DevicePool()
        self.ip1 = self.pool.get()
        self.ip2 = self.pool.get()
        self.v = Assert()
        self.driver = TeamPage(U2().u2(self.ip1))
        self.target = TeamPage(U2().u2(self.ip2))

    def setup(self):
        self.pics = []
        self.target.startApp(self.package)
        self.driver.startApp(self.package)

    def teardown(self):
        self.pics = []
        self.driver.stopApp(self.package)
        self.target.stopApp(self.package)

    def teardown_class(self):
        self.pool.put(self.ip1)
        self.pool.put(self.ip2)



    @pytest.mark.P1
    @allure.title('邀请内部联系人')
    def test_invitation_inside(self):
        """
        邀请内部联系人
        """

        self.target.login(**self.targetUserInfo)
        self.pics.append(self.driver.login(**self.userInfo))
        self.pics.append(self.driver.quick_call(self.targetUserName))



