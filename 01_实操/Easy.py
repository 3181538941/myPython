#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2021/3/18
# @file 2.py

# a = [0] * 100
# i = 6
# i = int(i)
# while (i):
#     a[i] = str(input())
#     i -= 1
# for j in range(0, 6):
#     print(a[j], end=' ')


# print('1')    if   int(input()) % 2   else   print('0'


# b = int(input())
# print(b) if a > b else print(a)
# print((a - b)//2) if a > b else print((b - a)//2)
# 袜子
# a, b = map(int, input().split())
# print(b, (a - b) // 2, end=' ') if a > b else print(a, (b - a) // 2, end=' ')
#
# if a > b:
#     print(b, (a - b) // 2, end=' ')
# else:
#     print(a, (b - a) // 2, end=' ')

# if a != b:
#     if a < b:
#         print(a * 2 + 1 + c * 2)
#     else:
#         print(b * 2 + 1 + c * 2)
# else:
#     if a < b:
#         print(a * 2 + c * 2)
#     else:
#         print(b * 2 + c * 2)
#
# a,b,c = map(int,input().split())
# if a < b:
#     s = (a * 2 + c * 2)
# else:
#     s = (b * 2 + c * 2)
# if a != b:
#     s += 1
# print(s)


# 地板砖
# x = 0
# y = 0
# m, n, a = map(int, input().split())
# if n % a == 0 and m % a == 0:
#     x = n // a
#     y = m // a
# elif n % a != 0 and m % a == 0:
#     x = n // a + 1
#     y = m // a
# elif n % a == 0 and m % a != 0:
#     x = n // a
#     y = m // a + 1
# elif n % a != 0 and m % a != 0:
#     x = n // a + 1
#     y = m // a + 1
# print(x * y)

# a = input().split()
# print(a[1], end=' ')

# print(' '.join(input().split())[::-1])


# import math
#
# a1,a2=map(float,raw_input().split())
# b1,b2=map(float,raw_input().split())
# ab=math.sqrt(pow(a1-b1,2)+pow(a2-b2,2))
# print "{:.3f}".format(ab)

# n,m=map(int,raw_input().split())
# a=[0]*n
# a=int(input().join()
# flag=0  # type: int
# for i in range(n):
#     if m==a[i]:
#         flag+=1
# print flag


# def fab(n):
#     n1 = 1
#     n2 = 1
#     n3 = 1
#     if n < 1:
#         return -1
#     while (n - 2) > 0:
#         n3 = n2 + n1
#         n1 = n2
#         n2 = n3
#         n -= 1
#     return n3
#
#
# r = fab(400)
# print r






# def fun(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fun(n - 1) + fun(n - 2)
#
#
# r = fun(40)
# print r








# #汉诺塔
# def han(n,x,y,z):
#     if n==1:
#         print x,'->',z  #最后一个盘子移动到z上
#     else:
#         han(n-1,x,z,y)  #将n-1个盘子借助z移动到y上
#         print x,'->',z  #将最下面的从x移动到z上
#         han(n-1,y,x,z)  #将y上的n-1个盘子借助x移动到z上
# n=int(input())
# han(n,'A','B','C')
#
#
#





print('h')

