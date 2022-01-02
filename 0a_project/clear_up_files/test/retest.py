#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2021/12/31
# @file re.py
# word = """
# '1_马克思基本原理试题库(选择题)2021_leo.doc',
# '2021-2022-1期末公共基础课考试时间表(1).xls',
# Linux任务.md,
# Linux任务.pdf,
# Linux任务答案.md,
# Linux任务答案.pdf,
# linux任务带答案.md,
# Python正则表达式操作指南.epub,
# Snipaste_2021-12-27_09-44-48.png,
# treetest.png,
# 思政和研讨论文封皮模板.doc
# """

import re
import os
import random
import time

path = r'D:\0a.dataout\01_待处理'


def readFIle(path):
    fileNameList = os.popen(rf"dir {path} /b").readlines()
    begin = time.perf_counter()
    fileNameList = ''.join(fileNameList).splitlines() # time: 9.599999999942987e-06
    # for i in range(len(fileNameList)):  # time: 1.2000000000012001e-05
    #     fileNameList[i] = fileNameList[i].replace('\n','')
    end = time.perf_counter()
    print(fileNameList)
    print(end - begin)
    return fileNameList


readFIle(path)


# for i in fileNameList:
#     print(i)
# for i in range(len(fileNameList)):
#     fileNameList[i] = fileNameList[i][:-1]
# print(fileNameList)

# for word in range(21):
#     print(f'{word:02d}')


# list1=random.sample(list(range(1,101)),20)
# print(list1)
# 取20个随机的,不重复的文件(使用random模块) 将其放到val文件夹内, 其余放到train文件夹内
