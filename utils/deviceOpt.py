# -*- coding: utf-8 -*-

# @Time    : 2021/9/30 4:25 下午 
# @Author  : cyq
# @File    : deviceOpt.py
import time
from uiautomator2 import Device, ServerError, UiObjectNotFoundError, Direction
from utils.log import log
from typing import Union, Optional, Any


class DeviceOpt:

    def __init__(self, u: Device):
        """
        :param u: Device
        """
        self.device = u
        # 录入FastInputIME输入法
        self.device.set_fastinput_ime(True)

    def getDeviceInfo(self) -> dict:
        """
        :return:  device Info
        """
        info = self.device.info
        log.info(f"{info}")
        return info

    def getAppInfo(self, appName: str) -> dict:
        """
        get app info
        :param appName: app info
        :return: {'packageName': 'tech.tosee.app', 
        'mainActivity': 'tech.tosee.app.modules.welcome.WelcomeActivity', 
        'label': '同视', 'versionName': '2.10.0', 'versionCode': 271, 'size': 36366148}

        """
        info = self.device.app_info(appName)
        log.info(f"{info}")
        return info

    def getCurrentPackageName(self) -> dict:
        """
        :return: currentPackageName
        """
        currentPackageName = self.device.app_current()
        log.info(f"{currentPackageName}")
        return currentPackageName

    def getAppList(self, filter_opt: str = None) -> list:
        """
        Args:
            filter_opt: [-f] [-d] [-e] [-s] [-3] [-i] [-u] [--user USER_ID] [FILTER]
        Returns:
            list of apps by filter
        """
        _l = self.device.app_list(filter_opt)
        log.info(f"{_l}")
        return _l

    def getWindowsSize(self) -> tuple:
        """
        getWindowsSize
        :return: WindowsSize
        """
        w, h = self.device.window_size()
        log.info(f"{w, h}")
        return w, h

    def getWLAN(self):
        ip = self.device.wlan_ip
        log.info(ip)
        return ip

    def getText(self, **kwargs) -> Union[str, None]:
        """
         get text from field
        :param kwargs:
        :return:
        """
        text = self.device(**kwargs).get_text(2)
        log.info(text)
        return text.strip() if text else None

    def getEleAttr(self, target: str = None, **kwargs) -> Any:
        """
        获取元素属性
        :param target: target attr [visibleBounds,checked ]
        :param kwargs: ele
        :return:
        """
        info = self.device(**kwargs).info
        log.info(info)
        log.info(f"info{target}:{info[target]}")
        return info[target]

    def getCenter(self, **kwargs) -> Union[tuple, None]:
        """
        获取ui对象中心点
        :param kwargs:
        :return:  Union[tuple, None]
        """
        try:
            x, y = self.device(**kwargs).center()
            log.info(f"{x, y}")
            return x, y
        except UiObjectNotFoundError as e:
            log.error(repr(e))
            return None

    def getToast(self) -> Union[str, None]:
        """
        获取弹窗信息
        :return:
        """
        msg = self.device.toast.get_message(4)
        log.info(msg)
        return msg.strip() if msg else None

    def getBounds(self, **kwargs) -> tuple:
        """
        获取元素坐标
        """
        lx, ly, rx, ry = self.device(**kwargs).bounds()
        log.info(f"{lx, ly, rx, ry}")
        return lx, ly, rx, ry

    def install(self, url: str):
        """
        先卸载
        安装Apk
        :param url: apk url
        """
        try:
            self.uninstall(self.PACKAGE_NAME)

            log.info(url)
            self.device.app_install(url)
        except ServerError as e:
            log.error(repr(e))
            raise e

    def uninstall(self, package_name: str) -> bool:
        """
        unInstall
        :param package_name: package_name
        :return: bool
        """
        try:
            _res = self.device.app_uninstall(package_name=package_name)
            log.info(f"{_res}")
            return _res
        except Exception as e:
            log.error(repr(e))
            return False

    def startApp(self, package_name: str, activity: str = None) -> None:
        """
        判断 app 是否运行，
        如果运行中，杀死进程 重启app
        :param package_name: package_name
        :param activity: activity
        :return:
        """

        try:
            currentApp = self.getCurrentPackageName()
            if currentApp['package'].strip() == package_name:
                log.info(f"{currentApp['package']} running ..")
                self.stopApp(package_name)
            self.device.app_start(package_name=package_name, activity=activity, wait=True)
            log.info(f"{package_name} start success")
            time.sleep(1)
        except Exception as e:
            log.error(repr(e))
            return

    def stopApp(self, package_name: str) -> None:
        """
        停止app
        :param package_name: package_name
        :return: none
        """
        try:
            log.info(package_name)
            self.device.app_stop(package_name)
        except Exception as e:
            log.error(repr(e))
            return

    def clearApp(self, package_name: str) -> None:
        """ Stop and clear app data: pm clear """

        self.device.app_clear(package_name=package_name)

        log.info(f"[{self.clearApp.__name__}]: {package_name}")

    def screenON(self) -> None:
        """点亮"""

        self.device.screen_on()
        log.info(f"[{self.screenON.__name__}]")

    def screenOFF(self) -> None:
        """息屏"""
        self.device.screen_off()
        log.info(f"[{self.screenOFF.__name__}]")

    def screenShot(self, file_path: str = None) -> bytes:
        """
        :param file_path:  存储地址
        :return:
        """
        log.info("")
        return self.device.screenshot(filename=file_path, format="raw")

    def notification(self) -> None:
        """下拉打开通知"""
        self.device.open_notification()

    def quickSettings(self) -> None:
        """下拉打开快速设置"""
        self.device.open_quick_settings()

    def exist(self, **kw) -> bool:
        """
        判断元素是否存在
        :return: bool
        """
        flag = self.device(**kw).exists()
        log.info(f"{flag}")
        return flag

    def xpath_click(self, xpath: str) -> None:
        """
        使用xpath点击
        :param xpath: xpath
        :return: none
        """
        try:
            self.device.xpath(xpath).click()
            log.info(xpath)
        except UiObjectNotFoundError as e:
            log.error(repr(e))
            raise e

    def click(self, opt: str = "c", **kwargs) -> None:
        """
        click
        :param opt:
            c 默认 普通点击
            l 长按1s
            d 双击
        :param kwargs:
            text, textContains, textMatches, textStartsWith
            className, classNameMatches
            description, descriptionContains, descriptionMatches, descriptionStartsWith
            checkable, checked, clickable, longClickable
            scrollable, enabled,focusable, focused, selected
            packageName, packageNameMatches
            resourceId, resourceIdMatches
            index, instance
        :return: none
        :raise UiObjectNotFoundError
        """
        try:
            log.info(f"opt:{opt},{kwargs}")
            if opt  == "c":
                self.device(**kwargs).click(4)
            elif opt == "l":
                self.device(**kwargs).long_click(1)
            elif opt == "d":
                self.doubleClick(*self.getCenter(**kwargs), 0.1)
        except UiObjectNotFoundError as e:
            log.error(repr(e))
            raise e

    def coordinateClick(self, x: Union[float, int], y: Union[float, int]) -> None:
        """
        坐标点击
        :param x: x coordinate
        :param y: y coordinate
        :return: none
        """
        try:
            log.info(f"{x, y}")
            self.device.click(x, y)
        except Exception as e:
            log.error(repr(e))
            return

    def doubleClick(self, x: Union[float, int], y: Union[float, int], t: float = 0.2) -> None:
        """
        双击
        :param x:  x coordinate
        :param y: y coordinate
        :param t: duration default 0.2
        :return: none
        """

        try:
            log.info(f"{x, y, t}")
            self.device.double_click(x, y, t)
        except Exception as e:
            log.error(repr(e))
            return

    def longClick(self, x: Union[float, int], y: Union[float, int], t: float = 1.0) -> None:
        """
        长按
        :param x:  x coordinate
        :param y: y coordinate
        :param t: duration default 0.2
        :return: none
        """

        try:
            log.info(f"{x, y, t}")
            self.device.long_click(x, y, t)
        except Exception as e:
            log.error(repr(e))
            return

    def send(self, text: str, **kwargs) -> None:
        """
        1. click
        2. send text
        :param text: text
        :param kwargs: 点击元素
        :return: None
        """
        self.click(**kwargs)
        try:
            log.info(text)
            self.device.send_keys(text, clear=True)
        except UiObjectNotFoundError as e:
            log.error(repr(e))
            raise e

    def press(self, *args) -> None:
        """
        press key via name or key code. Supported key name includes:
        :param args:  home, back, left, right, up, down, center, menu, search, enter,
            delete(or del), recent(recent apps), volume_up, volume_down,
            volume_mute, camera, power.
        :return:
        """
        try:
            log.info(args)
            self.device.press(*args)
        except Exception as e:
            log.error(repr(e))
            return

    def swipe(self, fx: float, fy: float, tx: float, ty: float,
              steps: Optional[int] = 1) -> None:
        """

        :param fx: from position
        :param fy: from position
        :param tx: to position
        :param ty: to position
        :param steps: 1 steps is about 5ms, if set, duration will be ignore
        :return: none
        """
        log.info(f"{fx, fy, tx, ty}")
        self.device.swipe(fx=fx, fy=fy, tx=tx, ty=ty, steps=steps)

    def swipeExt(self, opt: Union[Direction, str]) -> None:
        """
        滑动
        :param opt:
            direction (str): one of "left", "right", "up", "bottom" or
                                    Direction.LEFT
                                    Direction.FORWARD # 页面下翻, 等价于 d.swipe_ext("up"), 只是更好理解
                                    Direction.BACKWARD # 页面上翻
                                    Direction.HORIZ_FORWARD # 页面水平右翻
                                    Direction.HORIZ_BACKWARD) # 页面水平左翻
            scale (float): percent of swipe, range (0, 1.0]
            box (tuple): None or [lx, ly, rx, ry]
            kwargs: used as kwargs in d.swipe
        :return: none
        """
        try:
            log.info(opt)
            self.device.swipe_ext(opt)
        except Exception as e:
            log.error(repr(e))
            return

    def pushFile(self, file_path: str, target_path: str) -> None:
        """
        上传文件
        :param file_path: 文件地址
        :param target_path: 目标地址
        :return: none
        """

        try:
            log.info(file_path)
            self.device.push(file_path, target_path)
        except IOError as e:
            log.error(repr(e))
            return

    def pullFile(self, target_path: str, file_path: str) -> None:
        """
        Pull file from device to local
        :param file_path: 文件地址
        :param target_path: 目标地址
        :return: none
        """

        try:
            self.device.pull(target_path, file_path)
        except FileNotFoundError as e:
            log.error(repr(e))
            return

    def check(self) -> None:
        """
        检查并维持设备端守护进程处于运行状态
        """
        self.device.healthcheck()

    def openUrl(self, url: str) -> None:
        """
        Open Scheme
        :param url: target url
        :return:none
        """
        try:
            log.info(url)
            self.device.open_url(url)
        except Exception as e:
            log.error(repr(e))
            return None

    def record(self, filePath: str):
        """
        录制
        :param filePath:
        :return:
        """
        log.info(filePath)
        self.device.screenrecord(filePath)
        time.sleep(10)
        self.device.screenrecord.stop()

    def scroll(self):
        log.info(f"")
        self.device(scrollable=True).scroll.toBeginning()


if __name__ == '__main__':
    from devicePool import DevicePool
    from u import U2

    d = DevicePool()
    a = DeviceOpt(U2.u2(d.get()))

    # a.startApp(package_name)
    # a.stopApp(package_name)
    a.getCurrentPackageName()
    # a.uninstall(package_name)
    # a.install(download)
    # a.send(text="18888888889", resourceId="tech.tosee.app:id/account_container")
    # a.check()
    # a.openUrl("https://www.baidu.com")
    # a.getWLAN()
    # a.press("up")
    # a.coordinateClick(0.523, 0.5)
    # a.swipe(0.561, 0.048, 0.554, 0.462)
    # a.press("home")
    # a.swipeExt("down")
    # a.click(resourceId="tech.tosee.app:id/blank_view")
    # a.click(resourceId='tech.tosee.app:id/localVideoContainer')
    # a.getCenter(resourceId='tech.tosee.app:id/localVideoContainer')
    # a.getBounds(resourceId='tech.tosee.app:id/localVideoContainer')
    # a.swipe(1280, 80.0, 0.0, 80.0)
    # a.uninstall(package_name)
    # a.install(download)
    # a.startApp(package_name)
    # a.click("d",text="cyq")
    # a.swipeExt(Direction.BACKWARD)
    # a.click(resourceId="tech.tosee.app:id/call_button")
    # a.openUrl("https://cp.anyknew.com/")
    # a.screenShot("text.jpg")
    # a.stopApp(package_name)
    # a.getText(resourceId="tech.tosee.app:id/editTextAccount")
    # a.exist(resourceId="tech.tosee.app:id/tv_last_login_user")
    # a.getToast()
    # a.getText(resourceId="tech.tosee.app:id/tv_subtitle")
    # a.install(download)
    # a.getEleAttr("checked", resourceId="tech.tosee.app:id/teamSpaceCardView")
    # a.getEleAttr("visibleBounds", resourceId="tech.tosee.app:id/card_contact")
    # a.xpath_click('//*[@resource-id="tech.tosee.app:id/input_search_layout"]//android.widget.ImageButton[1]')
# [{'bounds': {'bottom': 380, 'left': 140, 'right': 410, 'top': 206}, 'childCount': 1, 'className': 'androidx.cardview.widget.CardView', 'contentDescription': None, 'packageName': 'tech.tosee.app', 'resourceName': 'tech.tosee.app:id/card_contact', 'text': None, 'visibleBounds': {'bottom': 380, 'left': 140, 'right': 410, 'top': 206}, 'checkable': True, 'checked': False, 'clickable': True, 'enabled': True, 'focusable': True, 'focused': False, 'longClickable': True, 'scrollable': False, 'selected': False}]
