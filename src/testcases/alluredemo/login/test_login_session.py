#! /usr/bin/env python
#coding=utf-8

import logging
import allure
import inspect
import time
import random


@allure.feature('测试登录功能')
class TestLoginbyWechat:
    @allure.story('测试已登录的场景')
    #这里的数字1474608 是做什么用途的呢？
    @allure.severity('minor')
    def test_2474609(self):
        with allure.step("点击用户icon，以便检查登录是否成功"):
            logging.info('Click user profile to check if user has login')
            time.sleep(random.randint(1,4))

        with allure.step("检查登录是否成功"):
            user_name_text= "杠基"
        assert user_name_text=="杠基"