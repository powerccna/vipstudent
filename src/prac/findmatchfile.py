#! /usr/bin/env python
#coding=utf-8

import os

class SearchFile:
    "Search file by special file suffix or file prefix"
    global filenamelist
    filenamelist = []

    def __init__(self):
        pass
        # self.filenamelist=[]

    def visit(self, arg, dirname, names, flist=filenamelist):
        # flist=self.filenamelist
        flist += [dirname + os.sep + file for file in names]

    def get_files_by_suffix(self, dictory, suffix):

        scriptfilelist = []
        os.path.walk(dictory, self.visit, 0)
        for script in filenamelist:
            if script.endswith(suffix) and os.path.isfile(script):
                scriptfilelist.append(script)
            else:
                pass
        # For filenamelist is global variable,if we use the multi method in this class
        # the filenamelist list include all search result, so we should empty it.
        del filenamelist[:]
        return scriptfilelist

    def get_files_by_prefix(self, dictory, prefix):
        scriptfilelist = []
        os.path.walk(dictory, self.visit, 0)
        for script in filenamelist:
            if os.path.basename(script).startswith(prefix) and os.path.isfile(script):
                scriptfilelist.append(script)
            else:
                pass
        del filenamelist[:]
        return scriptfilelist

    def get_match_dir(self, dictory, dir_name):

        match_dir_path = []
        os.path.walk(dictory, self.visit, 0)
        for dir in filenamelist:
            if os.path.isdir(dir) and os.path.basename(dir) == dir_name:
                match_dir_path.append(dir)
            else:
                pass
        del filenamelist[:]
        return match_dir_path

    def get_dirs_by_prefix(self, dictory, prefix):
        dir_list = []
        os.path.walk(dictory, self.visit, 0)
        for dir in filenamelist:
            if os.path.basename(dir).startswith(prefix) and os.path.isdir(dir):
                dir_list.append(dir)
            else:
                pass
        del filenamelist[:]
        return dir_list

