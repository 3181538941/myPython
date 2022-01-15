#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2021/12/31
# @file File.py

import os




class ViewFile(object):
    def __init__(self, path, kwargs):
        self.allFile = {}
        for typ in kwargs.keys():
            self.allFile[typ] = []  # 按键初始化self.allFile
        for p in kwargs.values():
            if not os.path.isdir(p):  # 路径不是文件夹, 即不存在时 创建文件夹
                os.makedirs(p)
        self.path = path
        self.toMove = []  # 需要移动文件列表, [文件名, 所在目录, 绝对路径]
        self.clean1(path, kwargs)

    def viewTarget(self, dirPath):
        pass
        # todo view the goal dir and list files to judge
        fileList = os.listdir(dirPath)
        return fileList

    def clean_old(self, path, kwargs):
        fileList = os.listdir(path)
        for item in fileList:
            absPath = os.path.join(path, item)
            # todo walk
            if os.path.isdir(absPath):
                # todo append dirName
                self.clean(absPath, kwargs)
            else:
                for typ in kwargs.keys():
                    if item.endswith(typ):
                        if typ not in self.allFile.keys():
                            self.allFile[typ] = []
                        self.allFile[typ].append(item)
                        if item not in self.viewTarget(kwargs[typ]):
                            os.popen(rf'move {absPath} {kwargs[typ]}')
                            self.hasMoved.append(item)

    def clean1(self, path, kwargs):

        def isInKey(file, keyList):
            """
            判断文件是否在文件类型内
            :param file: 需要判断的文件名
            :param keyList: 文件类型, type: 用空格分隔的字符串
            :return: 在字符串内返回 True
            """
            for item in keyList.split():
                if file.endswith(item):
                    return 1
            return 0

        for typ in kwargs.keys():  # 按文件类型循环(文件扫描过程)
            for dirPath, dirNames, fileNames in os.walk(path):
                for file in fileNames:  # 在dirPath文件夹内循环
                    if dirPath != kwargs[typ] and isInKey(file, typ):  # 要查找的文件类型不在选定文件夹内
                        self.toMove.append([file, typ, dirPath, os.path.join(dirPath, file)])
                        # self.toMove.append(file)
                        self.allFile[typ].append(file)

                    # pprint(dirPath)
                    # pprint(dirNames)
                    # pprint(fileNames)
        first = lambda li: [_[0] for _ in li]
        self.toMoveFile = first(self.toMove)
        for item in self.toMove:  # 移动文件过程
            os.popen(rf'move "{item[3]}" "{kwargs[item[1]]}"')



# path = r'F:\03_Important\Python\0a_project\clear_up_files'
path = r'E:\Download\云盘缓存'

# dic = {'exe': r'E:\Download\exes',
#        'zip': r'E:\Download\Compressed',
#        'rar': r'E:\Download\Compressed'}
dic = {'exe'       : r'E:\Download\云盘缓存\Executable',
       'zip rar 7z': r'E:\Download\云盘缓存\Compressed'}

list = ViewFile(path, dic)
# pprint(list.allFile)
# print('toMove')+
# pprint(list.toMove)
for i in dic.keys():
    print(f'{i} 文件有 {len(list.allFile[i])} 个, 分别为:\n {list.allFile[i]}')
# print(list.toMoveFile)
print(f'移动了 {len(list.toMoveFile)} 个文件, 分别为:\n {list.toMoveFile}')

def isDir(path):
    print(path)
# import re
# import os
#
#
# class ViewFile(object):
#     def __init__(self, path, **kwargs):
#         self.allFile = []
#
#         self.path = path
#         self.viewFile(path,**kwargs)
#
#     def viewFile(self, path, **kwargs):
#         fileList = os.listdir(path)
#         for item in fileList:
#             absPath = os.path.join(path, item)
#             if os.path.isdir(absPath):
#                 # todo append dirName
#                 self.viewFile(absPath)
#                 pass
#             else:
#                 # file = os.path.split(absPath)[1]
#                 # todo move
#                 for typ in kwargs.keys():
#                     if item.endswith(typ):
#                         os.popen(rf'move {absPath} {kwargs[typ]}')
#                         self.allFile.append(item)
#                 # self.allFile.append(item)
#                 # if item.endswith('.7z'):
#                 #     os.system(rf'move {absPath} E:\Download\Compressed')
#                 #     self.allFile.append(item)
#                 # elif item.endswith('rar'):
#                 #     os.system(rf'move {absPath} E:\Download\Compressed')
#                 # else:
#                 #     os.system(rf'move {absPath} E:\Download\others')
#
#
# # path = r'F:\03_Important\Python\0a_project\clear_up_files'
# path = r'E:\Download'
#
# dic = {
#        'exe': r'E:\Download\exes'}
#
# list = ViewFile(path,**dic)
# # list.viewFile()
# print(list.allFile)
#
# # li = [[] for _ in range(10)]
# # li[1].append(2)
# # print(li)
#
#
# # l = os.listdir(r'E:\Download\LANDrop')
# # os.popen(r'move E:\Download\LANDrop\1637049307333.jpg E:\Download')
# # print(l)
#
