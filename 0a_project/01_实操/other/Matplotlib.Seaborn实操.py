#!/usr/bin/env python2
# -*- coding:utf-8 -*-
# @author Leo
# @date 2021/6/7
# @file Matplotlib.Seaborn实操.py
import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------------------
# 绘制线型图
# ----------------------------------------------------------

# 绘制余弦函数图
plt.style.use("seaborn-darkgrid")  # 选择图形主题(默认为全刻度)
# 共有5个主题:暗网格(darkgrid), 白网格(whitegrid), 全黑(dark), 全白(white),全刻度
x = np.arange(0, 3 * np.pi, 0.1)  # 生成数组x
y = np.sin(x)  # 对于x中的每个元素取正弦值
plt.plot(x, y)  # 根据传入的数据,绘制曲线图
plt.show()  # 显示图形

# 绘制子图
plt.style.use("seaborn-whitegrid")
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)  # 生成正弦数据
y_cos = np.cos(x)  # 生成余弦数据
# 在当前图中添加子图, (2,1,1): 将原图分为2行1列两个子图, 后面的1表示选中第一个
plt.subplot(2, 1, 1)  # 第一个画板的第一个子图
plt.plot(x, y_sin)  # 绘制第一个子图
plt.title('Sine')  # 设置图的标题
plt.subplot(2, 1, 2)  # 第二个子图
plt.plot(x, y_cos)  # 绘制第二个子图
plt.title('Cosine')  # 设置图的标题
plt.show()

# 修改参数
plt.style.use("seaborn-dark")
plt.figure(figsize=(8, 6), dpi=80)  # 创建一个8*6大小的图像, dpi = 80 表示分辨率每英尺80点
# 创建一个1*1的子图
plt.subplot(111)  # 等价与(1,1,1)
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
# 绘制一个蓝色的,线宽为1个像素的余弦曲线,设置标签Blue,linestyle表示曲线的样式
plt.plot(X, C, color="blue", linewidth=1.0, label="Blue", linestyle="--")
# 绘制一个绿色的,线宽为1个像素的正弦曲线,设置标签Green,linestyle表示曲线的样式
plt.plot(X, S, color="green", linewidth=1.0, label="Green", linestyle="-.")
plt.legend()  # 设置显示的图例
plt.xlim(-4.0, 4.0)  # 设置x周范围
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))  # 设置x轴刻度
plt.ylim(-1.0, 1.0)  # 设置y周范围
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))  # 设置y轴刻度
plt.show()

# 改变颜色和线宽
plt.figure(dpi=80)
plt.plot(X, C, color="blue", linewidth=3.5, linestyle="--")  # 宽度为3.5的蓝色曲线
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")  # 宽度为2.5的红色曲线
plt.show()


# ----------------------------------------------------------
# 绘制散点图
# ----------------------------------------------------------

# Matplotlib实现散点图
a = np.random.randint(0, 20, 15)
b = np.random.randint(0, 20, 15)
print(a)
print(b)
plt.scatter(a, b)
plt.show()

# Seaborn实现散点图
df = pd.DataFrame({'x': a, 'y': b})  # 转化为DataFrame
sns.jointplot(x='x', y='y', data=df)  # 绘制散点图, x,y指定数据作为x,y轴的列ming
plt.show()


# ----------------------------------------------------------
# 绘制柱状图
# ----------------------------------------------------------

# Matplotlib实现柱状图
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文不显示的问题
level = ['perfect', 'god', '666']
x = range(len(level))  # 横坐标
y = [1, 3, 2]  # 纵坐标
plt.figure(dpi=100)  # 创建画布
plt.bar(x, y, width=0.5, color=['y', 'g', 'b'])  # 绘制柱状图
plt.xticks(x, level)  # 修改x轴的坐标显示
plt.grid(linestyle='--', alpha=0.5)  # 添加网格显示
plt.show()

# Seaborn实现柱状图
df1 = pd.DataFrame(['prefect', 'good', '666', '666', 'good', 'good'], columns=['level'])
sns.countplot(x='level', data=df1)  # 绘制柱状图
plt.show()


# ----------------------------------------------------------
# 绘制直方图
# ----------------------------------------------------------

# Matplotlib实现直方图
t = np.random.randint(0, 30, 90)
print(t)
plt.figure(dpi=100)
distance = 2  # 设置组距
group_num = int((max(t) - min(t)) / distance)  # 计算组数
plt.hist(t, facecolor='blue', edgecolor='black', alpha=0.7)  # 绘制直方图
plt.xticks(range(min(t), max(t))[::2])  # 修改x轴刻度显示
plt.grid(linestyle='--', alpha=0.5)  # 添加网格显示
plt.show()

# Seaborn实现直方图
sns.displot(t, kde=True)  # kde表示核密度， 图中的那条曲线
plt.show()
