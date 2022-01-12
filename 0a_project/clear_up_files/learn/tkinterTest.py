#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/1/8
# @file tkinterTest.py
import tkinter as tk
import os
from pprint import pprint

class ViewFile(object):
    def __init__(self, path, **kwargs):
        self.allFile = {}
        self.path = path
        self.viewFile(path,**kwargs)

    def viewFile(self, path, **kwargs):
        fileList = os.listdir(path)
        for item in fileList:
            absPath = os.path.join(path, item)
            if os.path.isdir(absPath):
                # todo append dirName
                self.viewFile(absPath,**kwargs)
                pass
            else:
                # file = os.path.split(absPath)[1]
                # todo move
                for typ in kwargs.keys():
                    if item.endswith(typ):
                        if typ not in self.allFile.keys():
                            self.allFile[typ] = []
                        self.allFile[typ].append(item)

                        # os.popen(rf'move {absPath} {kwargs[typ]}')



# path = r'F:\03_Important\Python\0a_project\clear_up_files'
path = r'E:\Download'

dic = {'exe': r'E:\Download\exes',
       'zip':'',
       'rar':''}

list = ViewFile(path,**dic)
# list.viewFile()
pprint(list.allFile)