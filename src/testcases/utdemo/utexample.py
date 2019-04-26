#!/usr/bin/env python
#encoding: utf-8
#author: Jim Yin

import unittest


class MyClass(object):
    def __init__(self, num):
        self.num = num

    def printNum(self):
        return self.num


class TestMyClass(unittest.TestCase):
    def test_printNum(self):
        value = MyClass(6)
        self.assertEquals(7, value.printNum())  # 当assertEquals失败时，会把第一个和第二个参数的值打印出来
        self.assertFalse(value.printNum() == 6)  # assertFalse和assertTrue不会打印值


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMyClass)
    unittest.TextTestRunner(verbosity=2).run(suite)