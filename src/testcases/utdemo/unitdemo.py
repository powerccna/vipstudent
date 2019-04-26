#!/usr/bin/env python
# encoding: utf-8
import unittest

def add(x, y):
    return x+y

class TAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_add2(self):
        self.assertEqual(add(1, 2), 4)

    def test_add3(self):
        self.assertEqual(add('tester', 'home'), 'testerhome')