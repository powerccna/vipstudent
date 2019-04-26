#!/usr/bin/env python
# encoding: utf-8
import pytest

@pytest.fixture()
def loginandlogout():
    print('do login action\n')
    yield
    print("do logout action\n")

class TestSample:

    @pytest.mark.usefixtures('loginandlogout')
    def test_answer(self):
        print("I am test answer\n")
        assert 1+9 == 10

    @pytest.mark.usefixtures('loginandlogout')
    def test_answer2(self):
        print("I am test answer2\n")
        assert 2+9 == 11