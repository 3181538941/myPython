#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/3/10
# @file 03_线程之间共享全局变量数据错误的问题.py
import threading
import time, os
g_num = 0

def task1():
    for i in range(1000000):
        global g_num
        g_num += 1
    print(f"task1: ",g_num)

def task2():
    for i in range(1000000):
        global g_num
        g_num += 1
    print(f"task2: ", g_num)

if __name__ == '__main__':
    fir = threading.Thread(target=task1)
    sec = threading.Thread(target=task2)
    fir.start()
    # 线程等待, 不加出问题原因: 两个线程可能同时处理数据, 使得数据被操作次数减少
    fir.join()

    sec.start()
