# -*- coding: utf-8 -*-

# @Time    : 2021/10/13 2:26 下午 
# @Author  : cyq
# @File    : baseEle.py


class BaseElements:
    # 现在通话
    BUTTON_CALL = {"resourceId": "tech.tosee.app:id/call_button"}

    # 收藏 or 取消收藏
    BUTTON_FAVORITE = {"resourceId": "tech.tosee.app:id/favorite_button"}

    # 删除
    BUTTON_DELETE = {"resourceId": "tech.tosee.app:id/delete_button"}

    # input_contact
    INPUT_CONTACT = {"resourceId": "tech.tosee.app:id/account_container"}

    # 确认添加
    BUTTON_SAVE = {"resourceId": "tech.tosee.app:id/save_button"}

    # 取消按钮
    BUTTON_CANCEL = {'resourceId': "tech.tosee.app:id/button_cancel"}

    # 下滑菜单 && 搜索
    DROP_CONTACT = {"resourceId": "tech.tosee.app:id/text_input_end_icon"}

    # 取消邀请
    BUTTON_CALL_CANCEL = {"resourceId": "tech.tosee.app:id/btn_cancel"}

    # 确认
    BUTTON_OK = {"resourceId": "tech.tosee.app:id/ok_button"}

    # 取消
    BUTTON_NO = {'resourceId': "tech.tosee.app:id/cancel_button"}

    # 进入空间文案
    TEXT_ENTER_SPACE = {"resourceId": "tech.tosee.app:id/enter_secret_text"}

    # 设置退出
    BUTTON_QUIT = {"resourceId": "tech.tosee.app:id/btn_logout"}

    # 弹窗信息
    SNACKBAR_TEXT = {"resourceId": "tech.tosee.app:id/snackbar_text"}

    # 搜索返回
    SEARCH_BACK = {'resourceId': "tech.tosee.app:id/ib_search_back"}

    # 设置layout
    LAYOUT_SETTING = {'resourceId': "android:id/content"}

    # setting userInfo
    TEXT_SETTING_USERINFO = {"resourceId": "tech.tosee.app:id/tv_user_info"}

    # setting merchant
    TEXT_MERCHANT = {"resourceId": "tech.tosee.app:id/tv_merchant_info"}

    # setting version
    TEXT_VERSION = {"resourceId": "tech.tosee.app:id/tv_app_version"}

    # 设置
    BUTTON_SETTING = {"resourceId": "tech.tosee.app:id/button_setting"}

    # 更新
    BUTTON_SETTING_UPDATE = {'resourceId': "tech.tosee.app:id/text_update"}
    # 上传日志
    BUTTON_UPLOAD = {'resourceId': "tech.tosee.app:id/rl_logs_upload_container"}

    # 更多设置
    BUTTON_MORE_SETTING = {'resourceId': "tech.tosee.app:id/rl_more_setting"}

    # 上传日志
    TEXT_UPLOAD = {"resourceId": "tech.tosee.app:id/text_info"}
    # 更新—检查-版本
    BUTTON_SETTING_UPDATE_CHECK_VERSION = {'resourceId': "tech.tosee.app:id/btn_tosee_check_version"}
    # 更新-检查-系统
    BUTTON_SETTING_UPDATE_CHECK_SYSTEM = {"resourceId": "tech.tosee.app:id/btn_tosee_check_system_version"}

    # 选择公司
    @staticmethod
    def CHOICE_COMPANY(company: str) -> dict:
        """
        选择公司
        :param company: 公司名
        :return:
        """
        return {"text": company}
