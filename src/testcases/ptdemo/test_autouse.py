#!/usr/bin/env python
# encoding: utf-8
import pytest

@pytest.fixture(scope='module',autouse=True)
def loginandlogout():
    print('do login action\n')
    yield
    print("do logout action\n")

@pytest.fixture(scope='class',autouse=True)
def clickhome():
    print('click home button\n')
    yield
    print("end home  button\n")

class TestSample:
    def test_answer(self):
        print("I am test answer\n")
        assert 1+9 == 10

    def test_answer2(self):
        print("I am test answer2\n")
        assert 2+9 == 11

class TestSampleTwo:

    def test_two_answer(self):
        print("I am test answer in test sample two\n")
        assert 1+9 == 10

    def test_two_answer2(self):
        print("I am test answer2 in test sample two\n")
        assert 2+9 == 11

    def test_itme(self):
        print("I am test itme in test sample two\n")
        assert 2+9 == 11