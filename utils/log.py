# -*- coding: utf-8 -*-

# @Time    : 2021/8/12 3:28 下午 
# @Author  : cyq
# @File    : log.py


import logging
import os
import time


def get_cwd():
    path = os.path.split(os.path.dirname(__file__))[0]
    # 当前文件的绝对路径
    return path



class ILog(object):


    def __init__(self, logger=None):


        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.handlers.clear()
        self.logger.setLevel(logging.INFO)
        # 创建一个handler，用于写入日志文件
        # 日期文件夹路径
        self.log_path = get_cwd()
        self.log_time = time.strftime("%Y-%m-%d")
        date_file_path = os.path.join(os.path.join(get_cwd(), 'logs'), self.log_time)

        # 如果没有日期文件夹，创建该文件夹
        if not os.path.exists(date_file_path):
            os.makedirs(date_file_path)
        # 完整日志存放路径
        all_log_path = os.path.join(date_file_path, 'allLogs/')
        # 如果没有完整日志文件夹，创建该文件夹
        if not os.path.exists(all_log_path):
            os.makedirs(all_log_path)
        # 错误日志存放路径
        error_log_path = os.path.join(date_file_path, 'errLogs/')
        if not os.path.exists(error_log_path):
            os.makedirs(error_log_path)

        self.all = all_log_path + self.log_time + '.log'
        self.err = error_log_path + self.log_time + '.log'


        fh = logging.FileHandler(self.all, 'a', encoding='utf-8')  # 这个是python3的
        eh = logging.FileHandler(self.err, 'a', encoding='utf-8')  # 这个是python3的

        fh.setLevel(logging.INFO)
        eh.setLevel(logging.ERROR)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] -> %(filename)s -> %(funcName)s -> [%(message)s]  ')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(eh)
        self.logger.addHandler(ch)


        # 关闭打开的文件
        fh.close()
        ch.close()
        eh.close()

    @property
    def log(self):
        return self.logger


log = ILog().log
