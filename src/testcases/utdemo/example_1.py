#!/usr/bin/env python
# encoding: utf-8

import unittest


class simple_test(unittest.TestCase):
    def setUp(self):
        print ("init")
        self.foo = list(range(10))
        print(str(self.foo))

    def test_1st(self):
        print('test_1st')
        self.assertEqual(self.foo.pop(), 10)

    # def test_2nd(self):
    #     print('test_1nd')
    #     self.assertEqual(self.foo.pop(), 9)

    def tearDown(self):
        print ("end method")


if __name__ == '__main__':
    unittest.main()