#!/usr/bin/env python
# encoding: utf-8
import pytest

#@pytest.fixture(scope='module',autouse=False)
# fixture就是为了测试用例的执行，而初始化一些数据和方法
@pytest.fixture()
def loginandlogout():
    print('\ndo login action\n')
    yield
    print("do logout action\n")

class TestSample:

    def test_answer(self,loginandlogout):
        print("I am test answer........\n")
        assert 1+9 == 10

    def test_answer2(self,loginandlogout):
        print("I am test answer2********\n")
        assert 1+10 == 11


class TestSample2:

    def test_answer2_1(self,loginandlogout):
        print("I am test answer\n")
        assert 1+9 == 10

    def test_answer2_2(self,loginandlogout):
        print("I am test answer2\n")
        assert 1+10 == 11