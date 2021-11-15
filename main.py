# -*- coding: utf-8 -*-

# @Time    : 2021/10/9 9:44 上午 
# @Author  : cyq
# @File    : main.py
import os

from utils.log import log
from utils.devicePool import DevicePool


# python3 -m weditor


def initAtx():
    """手动推送atx"""
    from config.Config import config
    from utils.shell import Shell
    ips = config.get_conf("address", "ip")
    for i in ips:
        Shell.invoke(f"/Users/yongqi/Library/Android/sdk/platform-tools/adb connect {i}")
    o = Shell.invoke(f"python3 -m uiautomator2 init")
    if o.count("Successfully") != len(ips):
        log.error("init atx error ->" + o)
        raise o


def initPackAge():
    """安装app"""
    from config.Config import config
    from utils.u import U2
    from utils.deviceOpt import DeviceOpt
    ips = config.get_conf("address", "ip")
    package = config.get_conf("application", "package_url")
    try:
        for ip in ips:
            d = DeviceOpt(U2().u2(ip))
            d.install(package)

    except Exception as e:
        log.error(repr(e))
        raise e


if __name__ == '__main__':
    import pytest as pt
    import sys
    from config.Config import config
    from utils.shell import Shell

    params = sys.argv
    # main host package level
    if len(params) > 2:
        config.set_conf("address", "ip", params[1])
        config.set_conf("application", "package_url", params[2])
        level = params[2]

    caseDir = "testcases/testCollection.py::TestCollection"
    args = ["-s", "-v", caseDir, '--alluredir', config.xml_report_path, '--clean-alluredir']
    initPackAge()
    # pt.main(args)
    #
    # if os.path.exists(config.html_report_path):
    #     Shell.invoke('rm -r %s' % config.html_report_path)
    # cmd = './allure-2.13.6/bin/allure generate %s -o %s --clean' % (config.xml_report_path, config.html_report_path)
    # Shell.invoke(cmd)
