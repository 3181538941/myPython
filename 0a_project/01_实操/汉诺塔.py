#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2021/3/23
# @file 汉诺塔.py
def han(n,x,y,z):
    if n==1:
        print(x,'->',z) #最后一个盘子移动到z上
    else:
        han(n-1,x,z,y)  #将n-1个盘子借助z移动到y上
        print (x, '->', z)  #将最下面的从x移动到z上
        han(n-1,y,x,z)  #将y上的n-1个盘子借助x移动到z上
n=int(input())
han(n,'A','B','C')
