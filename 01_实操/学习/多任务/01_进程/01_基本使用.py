#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/2/27
# @file 01_基本使用.py
import multiprocessing as mp
import time, os


def dance():
    # 获取当前进程的编号
    dance_id = os.getpid()
    # 获取当前进程对象
    print(f"dance_id: {dance_id}, {mp.current_process()}")
    # 获取当前进程的父进程编号
    print(f"parent of dance: {os.getppid()}")

    for _ in range(3):
        print('跳舞中...')
        time.sleep(0.2)
        # 根据进程号强制杀死指定进程
        os.kill(dance_id, 9)


def sing():
    # 获取当前进程的编号
    sing_id = os.getpid()
    # 获取当前进程对象
    print(f"sing_id: {sing_id}, {mp.current_process()}")

    for _ in range(3):
        print('唱歌中...')
        time.sleep(0.2)


if __name__ == '__main__':
    # 获取主进程id
    main_id = os.getpid()
    # 获取当前进程对象
    print(f"main_id: {main_id}, {mp.current_process()}")
    # 创建子进程
    dance_process = mp.Process(target=dance, name="dance")
    sing_process = mp.Process(target=sing, name="sing")
    # 启动进程
    dance_process.start()
    sing_process.start()
