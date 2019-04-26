#!/usr/bin/env python
# encoding: utf-8
#author: Jim Yin

import htmltestrunner
import unittest
from ut import example_1
from ut import  example_class
report_title = '执行报告'
desc = '测试用例执行报告'
report_file = 'ExampleReport.html'
testsuite = unittest.TestSuite()
testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(example_1.simple_test))
testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(example_class.simple_test))

with open(report_file, 'wb') as report:
    runner = htmltestrunner.HTMLTestRunner(stream=report, title=report_title, description=desc)
    runner.run(testsuite)