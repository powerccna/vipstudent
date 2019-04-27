#! /usr/bin/env python
#coding=utf-8


'''
搜索目录/home/tools/下所有已test开头，py结尾的文件(包括子目录的),
把文件全路径输出到一个列表里面打印出来
'''
import os

def get_files_by_prefix_postfix(path,match_prefix=None,match_postfix=None):
    '''

    :param path:
    :param match_prefix:
    :param match_postfix:
    :return: return list which files match prefix or postfix
    '''
    match_files = []
    for root, dirs, file_names in os.walk(path):
        for file_name in file_names:
            # match_prefix has value and match_postfix is None
            if match_prefix and not match_postfix:
                if file_name.startswith(match_prefix):
                    match_files.append(os.path.join(root, file_name))

            if not match_prefix and match_postfix:
                if file_name.endswith(match_postfix):
                    match_files.append(os.path.join(root, file_name))

            if match_prefix and match_postfix:
                if file_name.startswith(match_prefix) and \
                        file_name.endswith(match_postfix):
                    match_files.append(os.path.join(root, file_name))


    return match_files

print("%%"*20)
dir_path ='/data/ceba/gitee/vipstudent/src/testcases/'
print(get_files_by_prefix_postfix(dir_path,'test','.py'))
print(get_files_by_prefix_postfix(dir_path,'test'))
print(get_files_by_prefix_postfix(dir_path,match_postfix='.py'))