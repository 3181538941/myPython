#!/usr/bin/env python2
# -*- coding:utf-8 -*-
# @author Leo
# @date 2021/6/6
# @file Numpy实操.py
import numpy as np

# ----------------------------------------------------------
# Numpy元素的数据类型
# ----------------------------------------------------------
print(np.zeros([2, 2], dtype=int))  # 创建一个2*2的全0数组
print(np.ones([2, 2], dtype=int))  # 创建一个2*2的全1数组
print(np.eye(2, dtype=int))  # 创建一个2*2的对角线矩阵
print()
print(np.empty([3, 3]))  # 生成一个未初始化的3*3数组
print(np.full([3, 3], 6))  # 生成一个值全为6的3*3数组
print(np.linspace(0, 100, 10))  # 生成一个等间隔的数组，起始值0，终止值100，数量10
print()
a = np.array([1, 2, 3])  # 创建一维数组
print(a)
print(a.shape)  # shape为数组形状
print(a.size)  # size为数组元素


# ----------------------------------------------------------
# 索引和切片
# ----------------------------------------------------------
arr3 = np.arange(20).reshape((4, 5))  # reshape()方法改变数组形状
print("arr3: ", arr3)
print("arr的平均值: ", arr3.mean())  # mean()方法求平均值
print("arr的和: ", arr3.sum())  # sum()求和

arr = np.arange(10)
arr_slice = arr[5:8]  # 切片方式取值,类似与列表的切片
arr_slice[1] = 999
print(arr)  # [0 1 2 3 4 5 999 7 8 9]
arr_slice[:] = 14
print(arr)  # [0 1 2 3 4 14 14 14 8 9]
names = np.array(['Bob', 'Will', 'Bob', 'Joe'])
data = np.array([[-3, 2, 0, -1],
                 [1, 2, 3, -4],
                 [2.5, 1.7, -0.2, 1],
                 [-8, -4, 9, 10]])
print(data[names == 'Bob'])  # 根据True False选择数组内的数据
# [[-3.   2.   0.  -1. ]
#  [ 2.5  1.7 -0.2  1. ]]
print(data[names == 'Bob', 2:])
# [[ 0.  -1. ]
#  [-0.2  1. ]]


# ----------------------------------------------------------
# 基本统计方法
# ----------------------------------------------------------
arr3 = np.arange(20).reshape((4, 5))  # reshape()方法改变数组形状
print("arr3: ", arr3)
print("arr的平均值: ", arr3.mean())  # mean()方法求平均值
print("arr的和: ", arr3.sum())  # sum()求和

print("arr每行的平均值: ", arr3.mean(1))  # 对每行求平均值, 1表示行,0表示列
print("arr每列的平均值: ", arr3.sum(0))  # 对每列求和


# ----------------------------------------------------------
# 数组转置
# ----------------------------------------------------------
samples = np.random.normal(size=(2, 2))  # 生成一个2*2的随机数组
print(samples)
print("转置后的数组: ", samples.T)  # numpy.ndarry.T转置
