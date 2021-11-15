# -*- coding: utf-8 -*-

# @Time    : 2021/8/12 4:34 下午 
# @Author  : cyq
# @File    : assertOpt.py


from utils.log import log


class Assert:

    @staticmethod
    def assert_unequal(exp, res):
        try:
            assert exp != res
            log.info("ASSERT UNEQUAL: EXPECT IS [{}] RESULT IS [{}]".format(exp, res))

        except AssertionError as e:
            log.error("ASSERT UNEQUAL ERROR: EXPECT IS [{}] RESULT IS [{}]".format(exp, res))
            raise e

    @staticmethod
    def assert_equal(exp, res):

        try:
            assert exp == res
            log.info("ASSERT EQUAL: EXPECT IS [{}] RESULT IS [{}]".format(exp, res))

        except AssertionError as e:
            log.error("ASSERT EQUAL ERROR: EXPECT IS [{}] RESULT IS [{}]".format(exp, res))
            raise e

    @staticmethod
    def assert_in(exp, res):
        try:
            assert exp in res
            log.info("ASSERT IN: EXPECT IS [{}] RESULT IS [{}]".format(exp, res))
        except AssertionError as e:
            log.error("ASSERT IN ERROR: EXPECT IS [{}] RESULT IS [{}]".format(exp, res))
            raise e

    @staticmethod
    def assert_body(exp: dict, res: dict):

        for k, v in exp.items():
            if k in res:
                try:
                    assert res[k] == exp[k]
                    log.info(f"ASSERT BODY: EXPECT IS [{exp[k]}] RESULT IS [{res[k]}]")
                except AssertionError as e:
                    log.error(f"ASSERT BODY: EXPECT IS [{exp[k]}] RESULT IS [{res[k]}]")
                    raise e
            else:
                log.error(f"ASSERT BODY ERROR: RESULT BODY NON-EXISTENT [{k}] \n EXPECT IS [{exp}] RESULT IS [{res}]")
                raise AssertionError

    @staticmethod
    def assert_photo(exp_path: str, res_path: str):
        """
        判断两张图片
        """
        import cv2
        import numpy as np
        exp = cv2.imread(exp_path)
        res = cv2.imread(res_path)
        diff = cv2.subtract(exp, res)
        res = not np.any(diff)
        try:
            assert not np.any(diff) == True
            log.info(f"RES = {res}")
        except AssertionError as e:
            log.error(f"ASSERT BODY: EXPECT IS [{exp}] RESULT IS [{res}]")
            raise e
        finally:
            from pages.photos.photoOpt import del_photo
            del_photo(res_path)

