# -*- coding: utf-8 -*-

# @Time    : 2021/8/13 3:39 下午 
# @Author  : cyq
# @File    : deviceInfo.py


import re
import sys

from shell import Shell


class DeviceInfo:
    shell = Shell()

    def __init__(self):
        # 本人mac环境 adb需要绝对路径
        if sys.platform == "darwin":
            self.adbPath = "/Users/yongqi/Library/Android/sdk/platform-tools/"
        else:
            self.adbPath = ""

    def get_device_id(self) -> str:
        """
        :return: device_id
        """
        _cmd = self.adbPath + "adb devices | grep device | sed '1d' | awk '{print $1}'"
        device_id = self.shell.invoke(_cmd)
        return device_id.strip()

    def get_devices(self) -> []:
        """
         :return:  ID 列表
        """
        _cmd = self.adbPath + 'adb devices'
        devices = self.shell.invoke(_cmd)
        devices = devices.partition('\n')[2].replace('\n', '').split('\tdevice')
        return [device for device in devices if len(device) > 2]

    def get_android_version(self, deviceId) -> str:
        """
        :return: android_version
        """
        _cmd = self.adbPath + "adb -s %s shell getprop ro.build.version.release" % deviceId
        android_version = self.shell.invoke(_cmd).strip()
        return android_version

    def get_mobile_type(self, device_id) -> str:
        """
        :return:   mobile_type like: MI 8
        """
        _cmd = self.adbPath + "adb -s %s shell getprop ro.product.model" % device_id
        mobile_type = self.shell.invoke(_cmd).strip()
        return mobile_type

    def get_miui_version(self, device_id) -> str:
        """
        获取小米手机miui 版本
        :return: miui_version  like:9.5.27
        """
        _cmd = self.adbPath + "adb -s %s shell getprop ro.build.version.incremental" % device_id
        miui_version = self.shell.invoke(_cmd).strip()
        return miui_version

    def get_current_package_name(self, device_id) -> []:
        """
        :param device_id: device_id
        :return: 返回正在运行的程序 list[name activity]
        """
        _cmd = self.adbPath + "adb -s %s shell dumpsys window w | grep \/ | grep name" % device_id
        out = self.shell.invoke(_cmd)

        pattern = re.compile(r"[a-zA-Z0-9\.]+/.[a-zA-Z0-9\.]+")
        package_name = pattern.findall(out)[0].split("/")[0]
        package_name_activity = pattern.findall(out)[0].split("/")[1]
        current_app = []
        current_app.append(package_name)
        current_app.append(package_name_activity)
        return current_app

    def get_memory_total(self, device_id):
        """
        总内存
        :param device_id: device_id
        :return:  str 5632.09mb
        """
        _cmd = self.adbPath + "adb -s {}  shell cat /proc/meminfo".format(device_id)
        output = self.shell.invoke(_cmd)
        mem = re.findall(r'MemTotal:(.*?)kB', output)[0].strip()
        return str(round(float(mem) / 1024, 2)) + "mb"

    def get_memory_info(self, device_id, package_name) -> round:
        """
        获取指定app占有内存信息
        :param devices_id: device_id
        :param package_name: package_name
        :return: mem_size   like:364.91mb
        """
        _cmd = self.adbPath + 'adb -s %s shell dumpsys meminfo %s' % (device_id, package_name)
        me = self.shell.invoke(_cmd)
        print(me)
        mem_size = float(re.findall(r"TOTAL   (.*?)   ", me)[0]) / 1024
        return round(mem_size, 2)

    def get_battery(self, device_id) -> float:
        """
        :param device_id: device_id
        :return: battery_status   like:100
        """
        _cmd = self.adbPath + "adb -s %s shell dumpsys battery" % device_id
        output = self.shell.invoke(_cmd)
        battery = float(re.findall("level:.(\d+)*", output, re.S)[0])
        return battery

    def get_cup_info(self, device_id, package_name):
        """
        :param device_id: device_id
        :param package_name: package_name
        :return: CPU佔用：16%
        """
        _cmd = self.adbPath + 'adb -s %s shell dumpsys cpuinfo | grep %s' % (device_id, package_name)
        cpu_info = self.shell.invoke(_cmd)
        return cpu_info.split()[0]

    def get_pid(self, device_id, package_name):
        """
        :param device_id: device_id
        :param package_name: package_name
        :return: 进程PID like:6974
        """
        _cmd = self.adbPath + "adb -s %s  shell ps | grep %s" % (device_id, package_name)
        pid = self.shell.invoke(_cmd)
        return pid.split()[1]

    def get_app_pix(self, device_id):
        """
        手机分辨率
        Physical size ：物理尺寸
        Override size : 覆盖尺寸
        :param device_id: device_id
        :return: dict    {'Physical size': '1080x2158', 'Override size': '1080x2248'}
        """
        _cmd = self.adbPath + "adb -s {} shell wm size".format(device_id)
        info = self.shell.invoke(_cmd)
        size = info.split()[-1]
        return size

    def get_cpu_kel(self, device_id):
        """
        手机核数
        :param device_id: device_id
        :return: 8核
        """
        _cmd = self.adbPath + "adb -s {} shell cat /proc/cpuinfo".format(device_id)
        output = self.shell.invoke(_cmd)
        return str(len(re.findall("processor", output))) + "核"

    def get_app_version_name(self, device_id, package_name):
        """
        获取APP版本号
        :param device_id: device_id
        :param package_name: package_name
        :return:  like:  7.2.6
        """
        _cmd = self.adbPath + 'adb -s {} shell pm dump {} | grep versionName'.format(device_id, package_name)
        vn = self.shell.invoke(_cmd).split(' ')[-1].strip().split('=')[-1]
        return vn

    def get_log(self, psName):
        _cmd = self.adbPath + f"adb logcat | grep {psName}"
        log = self.shell.invoke(_cmd)
        return log

    def get_app_list(self, device_id):
        """
        get_app_list
        :return:  【"x","x"】
        """
        _cmd = self.adbPath + f"adb -s {device_id} shell pm list packages -3"
        o = self.shell.invoke(_cmd)
        return o.strip().split("\n")

    def connect(self, ip):
        """
        网络连接
        :param ip: ip
        :return:o
        """
        _cmd = self.adbPath + f"adb connect {ip}"
        o = self.shell.invoke(_cmd)
        return o

    def disconnect(self, ip):
        """
        disconnect
        :param ip: ip
        :return:
        """

        _cmd = self.adbPath + f"adb disconnect {ip}"
        o = self.shell.invoke(_cmd)
        return o

    def reboot(self, device_id):
        """

        :param device_id: device_id
        """
        _cmd = 'adb -s {} reboot'.format(device_id)
        self.shell.invoke(_cmd)

    def kill_app(self, pid):
        """
        杀死app进程
        :param pid:
        :return:
        """
        _cmd = self.adbPath + 'adb shell kill -9 {}'.format(pid)
        self.shell.invoke(_cmd)

    def start(self, device_id, packageName, activity):
        """
        open app
        :param device_id: device_id
        :param packageName: packageName
        :param activity: activity
        :return:
        """
        _cmd = self.adbPath + "adb -s %s shell am start -n %s/%s" % (device_id, packageName, activity)
        self.shell.invoke(_cmd)

    def stop(self, device_id, packageName):
        """
        stop
        :param device_id: device_id
        :param packageName: packageName
        :return:
        """
        _cmd = self.adbPath + f"adb -s {device_id} shell am force-stop {packageName}"
        self.shell.invoke(_cmd)
        return

    def install(self, apk_path: str, r="-r"):
        """
        install apk
        :param apk_path: apk_path
        :param r: if api is installed , reinstall APK and keep the data and cache files
        :return: o
        """
        _cmd = self.adbPath + "adb install {} {}".format(r, apk_path)
        o = Shell.invoke(_cmd)
        return o

    def uninstall(self, apk_path: str, k="-k"):
        """
        uninstall apk
        :param apk_path: apk_path
        :param k: uninstall app keep data and cache files
        :return: o
        """
        _cmd = self.adbPath + "adb uninstall {} {}".format(k, apk_path)
        o = Shell.invoke(_cmd)
        return o

    def clear_app_catch(self, device_id, apkName):
        """
        clear_app_catch
        :param apkName: apkName
        :return:
        """
        _cmd = self.adbPath + "adb -s {} shell pm clear {}".format(device_id, apkName)
        o = self.shell.invoke(_cmd)
        return o

    def kill_pid(self, device_id: str, pid: str):
        """
        kill_pid
        :param device_id: device_id
        :param pid: pid
        :return:
        """
        _cmd = self.adbPath + "adb -s {} shell kill {}".format(device_id, pid)
        o = self.shell.invoke(_cmd)
        return o


if __name__ == '__main__':
    d = DeviceInfo()
    id = d.get_device_id()
