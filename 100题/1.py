#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2021/3/18
# @file 1.py
for i in range(1, 5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            print(i * 100 + j * 10 + k)
