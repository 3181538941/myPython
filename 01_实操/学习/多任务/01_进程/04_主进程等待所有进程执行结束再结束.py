#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/3/6
# @file 04_主进程等待所有进程执行结束再结束.py

import multiprocessing as mp
import time

def task():
    for _ in range(8):
        print('执行中...')
        time.sleep(.2)




if __name__ == '__main__':
    # 创建子进程
    sub_process = mp.Process(target=task)
    # 设置子进程为守护主进程, 主进程在退出子进程后直接销毁
    # sub_process.daemon = True
    sub_process.start()

    time.sleep(1)
    # 退出子进程之前让子进程销毁
    sub_process.terminate()
    print("over")



