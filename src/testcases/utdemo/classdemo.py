#!/usr/bin/env python
# encoding: utf-8


import unittest


class simple_test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print ("setup method")
        self.foo = list(range(10))
        print(str(self.foo))

    def test_1st(self):
        print('test_1st')
        self.assertEqual(self.foo.pop(), 9)

    def test_2nd(self):
        print('test_2nd')
        print("test_2nd:"+str(self.foo))
        self.assertEqual(self.foo.pop(), 9)

    @classmethod
    def tearDownClass(self):
        print("end method")


if __name__ == '__main__':
    unittest.main()
