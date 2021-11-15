# -*- coding: utf-8 -*-

# @Time    : 2021/9/30 5:09 下午 
# @Author  : cyq
# @File    : u.py

import uiautomator2 as u
from uiautomator2 import ConnectError, Device
from utils.log import log


class U2:

    @classmethod
    def u2(cls, ip: str) -> [Device, None]:

        try:
            driver = u.connect(ip)
            log.info(f"[connect]->{ip}")
            # 设置元素查找等待时间（默认20s）
            driver.implicitly_wait(20.0)
            # 配置accessibility服务的最大空闲时间，超时将自动释放。默认3分钟。
            driver.set_new_command_timeout(300)
            return driver
        except ConnectError as e:
            log.error(repr(e))
            raise e


if __name__ == '__main__':
    # u = U2.u2()
    # print(u.info)
    from devicePool import DevicePool
    d3 = DevicePool()
    d3.get()
