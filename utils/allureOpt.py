# -*- coding: utf-8 -*-

# @Time    : 2021/10/20 5:33 下午 
# @Author  : cyq
# @File    : allureOpt.py
import json
from typing import Any
from utils.log import log
import allure


def allure_writer(func, pics: list, exp: Any = None, res: Any = None) -> None:
    """
    报告 写入
    :param func: 测试函数
    :param pics: 截图
    :param exp: 预期
    :param res: 结果
    """
    allure.attach(json.dumps(func.__name__, ensure_ascii=False), "case_name", allure.attachment_type.JSON)

    if func.__doc__:
        allure.attach(func.__doc__.strip(), 'Step',
                      allure.attachment_type.JSON)

    n = 0

    for i in pics:
        n += 1
        allure.attach(i, 'Step{}'.format(n), allure.attachment_type.PNG, f"step{i}")

    if exp and res:
        if isinstance(exp, str) and isinstance(res, str) and ".png" in exp and ".png" in res:
            # 图片
            from pages.photos.photoOpt import read_photo
            allure.attach(read_photo(exp), 'Expect ', allure.attachment_type.PNG)
            allure.attach(read_photo(exp), 'Actual ', allure.attachment_type.PNG)
        else:
            allure.attach(json.dumps(exp, ensure_ascii=False), 'Expect ', allure.attachment_type.JSON)
            allure.attach(json.dumps(res, ensure_ascii=False), 'Actual ', allure.attachment_type.JSON)

    log.info("===============  {} 测试完成  ===============    \n".format(func.__name__))
