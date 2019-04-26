#!/usr/bin/env python
# encoding: utf-8
#author: Jim Yin

import unittest

class simple_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("init class\n")
        simple_test.foo = list(range(10))
        print(str(simple_test.foo))

    def test_1st(self):
        print(str(simple_test.foo))
        self.assertEqual(simple_test.foo.pop(), 9)

    def test_2nd(self):
        print(str(simple_test.foo))
        self.assertEqual(simple_test.foo.pop(), 8)

    @classmethod
    def tearDownClass(cls):
        print("end class")

if __name__ == '__main__':
    unittest.main()