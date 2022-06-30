#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/3/10
# @file 04_互斥锁.py
import threading, time, os

g_num = 0
# 进程锁
lock = threading.Lock()


# 死锁: 其他线程一直等待释放进程锁的情景


def task1():
    # 上锁
    lock.acquire()
    global g_num
    for i in range(1000000):
        g_num += 1
    print(f"task1: {g_num}")
    # 释放锁
    lock.release()


def task2():
    # 上锁
    lock.acquire()
    global g_num
    for i in range(1000000):
        g_num += 1
    print(f"task2: {g_num}", )
    # 释放锁
    lock.release()


if __name__ == '__main__':
    fir = threading.Thread(target=task1)
    sec = threading.Thread(target=task2)
    fir.start()
    sec.start()
