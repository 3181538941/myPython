#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/3/10
# @file 01_多线程的使用.py
import threading
import time, os


def sing():
    # # 获取当前线程对象
    # current_thread = threading.current_thread()
    # print(current_thread)

    for i in range(3):
        print("singing...")
        time.sleep(.2)


def dance():
    # # 获取当前线程对象
    # current_thread = threading.current_thread()
    # print(current_thread)

    for i in range(3):
        print("dancing...")
        time.sleep(.2)


if __name__ == '__main__':
    # 获取当前线程对象
    current_thread = threading.current_thread()
    print(current_thread)

    # 创建子线程
    sing_thread = threading.Thread(target=sing, name='sing')
    dance_thread = threading.Thread(target=dance, name='dance')
    # 启动子线程
    sing_thread.start()
    dance_thread.start()
