#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2021/3/16
# @file 斐波那契数列.py
a = [1,2,3]
a[0] = 7
a[1] = 11
for i in range(3,100):
    s = a[i - 1] + a[i - 2]
    a.append(s)
for i in range(2,100):
    print(a,end=' ')
