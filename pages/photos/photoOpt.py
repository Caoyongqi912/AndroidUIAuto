# -*- coding: utf-8 -*-

# @Time    : 2021/10/27 2:34 下午 
# @Author  : cyq
# @File    : photoOpt.py

import os


def get_path(file: str) -> str:
    """
    获取图片地址
    :param file:
    :return:
    """
    path = os.path.join(os.path.dirname(__file__), file + ".png")
    return path


def del_photo(file: str) -> None:
    """
    删除图片
    :param file:
    :return: none
    """

    os.remove(path=os.path.join(os.path.dirname(__file__), file))


def read_photo(file: str) -> bytes:
    with open(file,mode="rb") as f:
        return f.read()
