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


