#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author Leo
# @date 2021/7/30
# @file 正反99乘法表.py

def multiplication(n=0):
    """
    打印九九乘法表

    参数:
        n = 0 正向输出;  n = 1 反向输出

    Return:
        无返回值
    """
    if n == 0:
        outside = range(1, 10)
    else:
        outside = range(9, 0, -1)
    for _ in outside:
        for j in range(1, _ + 1):
            print(f"{_}x{j}={_ * j}", end=" ")
        print()


multiplication()

# def transpose(iterable):
#     temp = []
#     for i in range(len(iterable)):
#         temp.append(iterable[i])
#     print(temp)
#     li = \
#     [[ 1,  2,  3,  4,  5],
#      [ 6,  7,  8,  9, 10],
#      [11, 12, 13, 14, 15],
#      [16, 17, 18, 19, 20],
#      [21, 22, 23, 24, 25]]
#     zipped = zip(li[0],li[1],li[2],li[3],li[4])
#     li_ = []
#     for i in zipped:
#         li_.append(i)
#     print(len(li))
#     print(li_)
#
# li = \
#     [[ 1,  2,  3,  4,  5],
#      [ 6,  7,  8,  9, 10],
#      [11, 12, 13, 14, 15],
#      [16, 17, 18, 19, 20],
#      [21, 22, 23, 24, 25]]
# # for i in zip(li):
#
# #     print(i)
# zi = zip(li)
# for i in zi:
#     print(i)


