#! /usr/bin/env python
#coding=utf-8

import subprocess

print(subprocess.check_output(["ls"," -al"],shell=True))
print("*"*10)
print(subprocess.call(["ls"," -al"],shell=True))
subprocess.Popen
