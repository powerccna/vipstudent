#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import pytest
import subprocess
import logging
import allure
import shutil


#为什么我们要设置这个路径到pythonPATH
sys.path.append(os.path.dirname(sys.modules[__name__].__file__))

fileHandler = logging.FileHandler(filename="../log/uiauto.log",encoding="utf-8")
logging.getLogger().setLevel(0)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
fileHandler.setFormatter(formatter)

logging.getLogger().addHandler(fileHandler)


if __name__ == '__main__':
    shutil.rmtree('../log/report/xml/')

    #pytest.main(['-sq', '--alluredir', '../log/testreport', 'testcases/myselector/test_all_stocks.py'])
    #pytest.main(['-sq', '--alluredir', '../log/testreport/xml', 'testcases/login','testcases/myselector'])
    #pytest.main(['--alluredir', '../log/report/xml','--allure_severities=blocker', 'testcases/'])
    pytest.main(['--alluredir', '../log/report/xml', 'testcases/alluredemo/login/test_login.py::TestLogin::test_2474609'])
    #pytest.main(['--alluredir', '../log/report/xml','--allure-severities=blocker', 'testcases/alluredemo/'])
    #pytest.main(['--alluredir', '../log/report/xml','--allure-features=测试登录功能', 'testcases/alluredemo/'])

    print(subprocess.getstatusoutput('/usr/local/bin/allure generate --clean ../log/report/xml -o ../log/report/html'))
