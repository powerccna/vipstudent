#!/usr/bin/env python
# encoding: utf-8
#author: Jim Yin
import pytest
import random

@pytest.fixture(scope="module",autouse=True)
def open():
    print("打开浏览器，并且打开百度首页")
    yield
    print("最后关闭浏览器")

def test_s1():
    print("用例1：搜索python-1")
    a=random.randint(1,3)
    print(a)
    assert 1==a

def test_s2():
    print("用例2：搜索python-2")

def test_s3():
    print("用例3：搜索python-3")

if __name__ == "__main__":
    pytest.main(["-s", "--reruns","3","test_teardown.py"])