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
path = r'D:\0a.dataout\01_待处理'
fileNameList = os.popen(rf"dir {path} /b").readlines()
print(fileNameList)
print(type(fileNameList))
for i in range(len(fileNameList)):
    fileNameList[i] = fileNameList[i][:-1]
print(fileNameList)
