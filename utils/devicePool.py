# -*- coding: utf-8 -*-

# @Time    : 2021/10/11 5:08 下午 
# @Author  : cyq
# @File    : devicePool.py

from config.Config import config
from queue import LifoQueue
from utils.log import log
from typing import Union


class DevicePool:
    __instance = None

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        self._dp = config.get_conf("address", "ip")
        self.dp = LifoQueue(maxsize=len(self._dp))
        for ip in self._dp:
            self.dp.put(ip)

    def get(self) -> Union[str, None]:
        """
        获取一个设备
        :return:
        """
        if self.dp.qsize() > 0:
            device = self.dp.get()
            log.info(device)
            return device
        else:
            log.error("device pool empty")
            return None

    def put(self, ip: str) -> None:
        """
        放入一个设备
        :param ip: 设备ip
        :return:
        """
        log.info(ip)
        self.dp.put(ip)

    def checkPool(self) -> bool:
        """
        检查设备池是否为空
        :return: bool
        """
        flag = self.dp.empty()
        log.info(f"{flag}")
        if not flag:
            return True
        else:
            return False

    def getPoolSize(self) -> int:
        """
        获取设备池长度
        :return:  size
        """
        size = self.dp.qsize()
        log.info(f"{size}")
        return size



if __name__ == '__main__':
    q = DevicePool()
    k1 = q.get()
    # q.put(k1)
    k2 = q.get()

