#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2021/12/31
# @file File.py

import re
import os


class ViewFile(object):
    def __init__(self, path, **kwargs):
        self.allFile = []

        self.path = path
        self.viewFile(path,**kwargs)

    def viewFile(self, path, **kwargs):
        fileList = os.listdir(path)
        for item in fileList:
            absPath = os.path.join(path, item)
            if os.path.isdir(absPath):
                # todo append dirName
                self.viewFile(absPath)
                pass
            else:
                # file = os.path.split(absPath)[1]
                # todo move
                for typ in kwargs.keys():
                    if item.endswith(typ):
                        os.popen(rf'move {absPath} {kwargs[typ]}')
                        self.allFile.append(item)
                # self.allFile.append(item)
                # if item.endswith('.7z'):
                #     os.system(rf'move {absPath} E:\Download\Compressed')
                #     self.allFile.append(item)
                # elif item.endswith('rar'):
                #     os.system(rf'move {absPath} E:\Download\Compressed')
                # else:
                #     os.system(rf'move {absPath} E:\Download\others')


# path = r'F:\03_Important\Python\0a_project\clear_up_files'
path = r'E:\Download'

dic = {
       'exe': r'E:\Download\exes'}

list = ViewFile(path,**dic)
# list.viewFile()
print(list.allFile)

# li = [[] for _ in range(10)]
# li[1].append(2)
# print(li)


# l = os.listdir(r'E:\Download\LANDrop')
# os.popen(r'move E:\Download\LANDrop\1637049307333.jpg E:\Download')
# print(l)

