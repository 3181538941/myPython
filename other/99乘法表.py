#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2021/2/5
# @file 99乘法表.py

i = 1
# while i <= 9:
for i in range(1,10):
    j = 1
    # while j <= i:
    for j in range(1,i):
        print(j,'*',i,'=',i * j,end='\t')
        j += 1
    print()
    i += 1
