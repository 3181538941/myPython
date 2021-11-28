#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2021/3/25
# @file main.py
class Stu:
    def __init__(self):
        __name = ''
        __age = 0
        __sex = '11'
        __num = 0

    def setname(self, name):
        self.__name = name

    def setage(self, age):
        self.__age = age

    def setsex(self, sex):
        self.__sex = sex

    def setnum(self, num):
        self.__num = num

    def getname(self):
        return self.__name

    def getage(self):
        return self.__age

    def getsex(self):
        return self.__sex

    def getnum(self):
        return self.__num

a = Stu()
a.setnum(12)
# b=a.getsex()
# print b
print a.getnum()