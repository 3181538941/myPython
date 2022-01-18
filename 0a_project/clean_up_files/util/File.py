#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2021/12/31
# @file File.py

import os


class ViewFile(object):

    def __init__(self, path, kwargs, deal='move', exceptList=None):
        # allFile用来记录扫描出的文件, {'后缀名': ['文件名', '文件名']}
        self.allFile = {}
        for typ in kwargs.keys():
            self.allFile[typ] = []  # 按键初始化self.allFile
        # 在文件夹不存在时 创建文件夹
        for p in kwargs.values():
            if not os.path.isdir(p):
                os.makedirs(p)
        # 需要移动文件列表, [文件名, 所在目录, 绝对路径]
        self.toMove = []
        # 要排除的文件
        if exceptList == None:
            exceptList = []
        self.exceptList = exceptList
        # 调用主要方法
        self.clean(path, kwargs, deal)

    def clean(self, path, kwargs, deal=None):
        """
        核心函数, 扫描符合要求的文件, 记录文件信息, 将其移动或复制文件到目标路径

        :param path: 要整理的文件夹路径
        :param kwargs: 键为文件类型值为目标路径的字典
        :param deal: 文件处理方式, 默认是
        :return:
        """

        def isInKey(file, keyList):
            """
            判断文件的后缀名是否在选定的文件类型内, (拆分文件类型字符串, 分别判断文件是否以其中的后缀名结尾)

            :param file: 需要判断的文件名
            :param keyList: 文件类型, type: 用空格分隔的字符串
            :return: 后缀名符合要求返回 True
            """
            fileNameSuffix = file.split('.')[-1]
            if fileNameSuffix in keyList:
                return 1
            return 0
            # for item in keyList.split():
            #     if file.endswith(item):
            #         return 1
            # return 0

        # allKey: 后缀名字符串, 用来判断其他情况, 放在循环外部防止多次调用浪费资源
        allKey = ''.join(kwargs.keys())
        key = 0  # 正常最外层是后缀名循环, 为防止判断其他文件时多次记录, 所以用此变量作为记录
        for typ in kwargs.keys():  # 按文件类型循环(文件扫描过程)
            for dirPath, dirNames, fileNames in os.walk(path):
                for file in fileNames:  # 在dirPath文件夹内循环
                    # 要查找的文件类型不在目标文件夹内, 文件类型符合要求, 文件不在排除的文件列表内
                    if dirPath != kwargs[typ] and isInKey(file, typ) and file not in self.exceptList:
                        # toMove: 存储文件信息的二维列表, [[文件名, 文件类型, 文件父路径, 文件绝对路径, 文件目标路径], ]
                        self.toMove.append([file,
                                            typ,
                                            dirPath,
                                            os.path.join(dirPath, file),
                                            kwargs[typ]]
                                           )
                        self.allFile[typ].append(file)
                    # 其他文件情况, 不在'其他'文件夹内, 不属于给定的任何一种文件类型, 且只在外层第一次循环时记录
                    elif dirPath != kwargs['others'] and not isInKey(file, allKey) and key == 0:
                        self.toMove.append([file,
                                            'others',
                                            dirPath,
                                            os.path.join(dirPath, file),
                                            kwargs['others']]
                                           )
                        self.allFile['others'].append(file)
                        pass
            key += 1

        first = lambda li: [_[0] for _ in li]
        self.toMoveFile = first(self.toMove)  # 需要移动的文件名列表
        # print(self.toMoveFile)
        # print(self.toMove)
        # print(self.allFile)
        if deal:
            for item in self.toMove:  # 移动文件过程
                # move 文件绝对路径 该文件类型应放的文件夹
                os.popen(rf'{deal} "{item[3]}" "{item[4]}"')


def isDir(path):
    """
    调用 os.path 判断传过来的路径是不是文件夹
    """
    return os.path.isdir(path)


if __name__ == '__main__':

    # path = r'F:\03_Important\Python\0a_project\clear_up_files'
    path = r'E:\Download\云盘缓存'

    dic = {'exe'             : r'E:\Download\云盘缓存\Executable',
           'zip rar 7z'      : r'E:\Download\云盘缓存\Compressed',
           'png jpg jpeg ico': r'E:\Download\云盘缓存\Pictures',
           'others'          : r'E:\Download\云盘缓存\Others'}

    fileTypeNameDic = {'exe'             : '可执行文件',
                       'zip rar 7z'      : '压缩包',
                       'png jpg jpeg ico': '图片',
                       'others'          : '其他文件'}

    exceptList = ['云盘缓存.zip']

    list = ViewFile(path, dic, 'move', exceptList=exceptList)
    list.exceptList = []
    for i in dic.keys():
        print(f'{fileTypeNameDic[i]}有 {len(list.allFile[i])} 个, 分别为:\n {list.allFile[i]}')
    print(f'移动了 {len(list.toMoveFile)} 个文件, 分别为:\n {list.toMoveFile}')

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
