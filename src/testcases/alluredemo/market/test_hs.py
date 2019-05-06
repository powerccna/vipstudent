#!/usr/bin/env python
# encoding: utf-8
import pytest
import logging
import allure

class TestHSMarket:
    @allure.severity('trivial')
    def test_increase_top(self):
        logging.info('start to execute increase top stock')
        assert False

    @allure.severity('blocker')
    def test_decrease_top(self):
        logging.info('start to execute decrease top stock')
        assert True