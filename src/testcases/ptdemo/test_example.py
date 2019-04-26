#!/usr/bin/env python
#encoding: utf-8

import pytest
import time
import random


@pytest.fixture(scope='module')
def count():
    print('init count')
    return 3


@pytest.mark.hello
@pytest.mark.P0
@pytest.mark.xiaoping
class TestSample:

    @pytest.mark.zhangting
    def test_answer(self, count):
        print('test_answer get count %s' % count)
        time.sleep(random.randint(1, 5))
        assert count == 3

    def test_answer_2(self, count):
        print('test_answer_2 get count %s' % count)
        time.sleep(random.randint(1, 5))
        assert count == 4

    def test_answer_3(self, count):
        print('test_answer_3 get count %s' % count)
        time.sleep(random.randint(1, 5))
        assert count == 2

@pytest.mark.webtest
@pytest.mark.P0
@pytest.mark.zhangting
@pytest.mark.mandy
class TestSample2:

    def test_answer4(self, count):
        print('test_answer4 get count %s' % count)
        time.sleep(random.randint(1, 5))
        assert count == 3

