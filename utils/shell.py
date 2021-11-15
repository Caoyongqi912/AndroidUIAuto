# -*- coding: utf-8 -*-

# @Time    : 2021/10/9 3:01 下午 
# @Author  : cyq
# @File    : shell.py


import subprocess

from utils.log import log


class Shell:

    @staticmethod
    def invoke(cmd):
        log.info(cmd)
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        e = errors.decode("utf-8")
        if o:
            log.info(f"o:{o}")
            return o
        elif e:
            log.error(f"e:{e}")
            return e
