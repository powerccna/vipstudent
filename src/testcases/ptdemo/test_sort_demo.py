#! /usr/bin/env python
#coding=utf-8

from testcases.ptdemo import sortdemo


def test_bubble_sort():
    assert sortdemo.bubble_sort([13,1,2,5,8,18])==[1, 2, 5, 8, 13, 18]
