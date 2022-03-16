#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/3/10
# @file 02_线程的执行是无序的.py
import threading
import time, os

def task():
    time.sleep(.5)
    print(threading.current_thread())



if __name__ == '__main__':
    for i in range(20):
        sub_thread = threading.Thread(target=task)
        sub_thread.start()
        # 线程的执行是无序的, 具体执行哪个线程是由CPU调度决定的