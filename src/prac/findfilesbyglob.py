#! /usr/bin/env python
#coding=utf-8

# -*- coding: UTF-8 -*-
import glob
import os.path


def traversalDir_FirstDir(path):
    list = []
    if (os.path.exists(path)):
        # 获取该目录下的所有文件或文件夹目录路径
        files = glob.glob(path + '/*.py')
        print(files)
        for file in files:
            # 判断该路径下是否是文件夹
            if (os.path.isdir(file)):
                # 分成路径和文件的二元元组
                h = os.path.split(file)
                list.append(h[1])
    print(list)


traversalDir_FirstDir("/data/ceba/gitee/vipstudent/src")