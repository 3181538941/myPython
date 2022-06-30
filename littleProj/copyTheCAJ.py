#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/6/1
# @file copyTheCAJ.py
from pyperclip import copy

text = """


"""
# 复制去除空格和回车的文本
s = ''.join([i for i in text if i != ' ' and i != '\n'])

print(s)
copy(s)
