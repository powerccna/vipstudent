#! /usr/bin/env python
#coding=utf-8

'''
查找/tomcat/log/ 目录下的log文件，如果文件最后修改时间是在1小时之前，
把次文件打包压缩，备份到/home/back/log 目录下
'''
import os
import subprocess

print(os.stat("demo.txt")[9])
print(subprocess.check_output(['tar -cvf tomat.tar log'],shell=True))

