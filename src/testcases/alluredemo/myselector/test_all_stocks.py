#! /usr/bin/env python
#coding=utf-8

import pytest
import allure
import logging
import time
import random


@pytest.fixture()
def login_xueqiu():
    logging.info('Logging xueqiu')
    yield
    logging.info('loggout xueqiue')


@pytest.mark.usefixtures("login_xueqiu")
@allure.feature('测试我的自选')
class TestMySelector:
    @allure.story('测试我的股票/全部选项页面数据，能展示香港的股票')
    @allure.severity('critical')
    #这里的数字1474608 是做什么用途的呢？
    def test_2474610(self):

        with allure.step("点击我的自选tab，切换我的自选页面"):
            logging.info('切换到自选页面')
            time.sleep(random.randint(1,3))

        with allure.step("点击股票选项"):
            time.sleep(random.randint(1, 3))

        with allure.step("点击全部选项"):
            time.sleep(random.randint(1, 3))

        with allure.step("获取全部的股票名字"):
            logging.info('正在获取股票码')
            time.sleep(random.randint(1, 3))
            stocks_code = ['01816','600100','510300']

        assert "01816" in stocks_code

    @allure.story('测试我的股票/全部选项页面数据，能展示指数基金')
    # 这里的数字1474608 是做什么用途的呢？
    def test_2474611(self):
        with allure.step("点击我的自选tab，切换我的自选页面"):
            logging.info('切换到自选页面')
            time.sleep(random.randint(1, 3))

        with allure.step("点击股票选项"):
            time.sleep(random.randint(1, 3))

        with allure.step("点击全部选项"):
            time.sleep(random.randint(1, 3))

        with allure.step("获取全部的股票名字"):
            logging.info('正在获取股票码')
            time.sleep(random.randint(1, 3))
            stocks_code = ['01816', '600100', '510300']

        assert "510300" in stocks_code

    @allure.story('测试我的股票/全部选项页面数据，能展示沪市基金')
    # 这里的数字1474608 是做什么用途的呢？
    def test_2474612(self):
        with allure.step("点击我的自选tab，切换我的自选页面"):
            self.info = logging.info('切换到自选页面')
            time.sleep(random.randint(1, 3))

        with allure.step("点击股票选项"):
            time.sleep(random.randint(1, 3))

        with allure.step("点击全部选项"):
            time.sleep(random.randint(1, 3))

        with allure.step("获取全部的股票名字"):
            logging.info('正在获取股票码')
            time.sleep(random.randint(1, 3))
            stocks_code = ['01816', '600100', '510300']

        assert "600111" in stocks_code
