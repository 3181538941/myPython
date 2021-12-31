#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2021/12/31
# @file File.py

import re
import os

def readFileNames(path = r'D:\0a.dataout\01_待处理'):
    fileNameList = os.popen(rf"dir {path} /b").readlines()
    print(fileNameList)
    print(type(fileNameList))
    for i in range(len(fileNameList)):
        fileNameList[i] = fileNameList[i][:-1]
    print(fileNameList)