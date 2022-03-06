#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/3/6
# @file 03_进程之间不共享全局变量.py
import multiprocessing as mp
import time
# 全局变量
pub_list = list("123")

def add_proc():
    for each in "abc":
        pub_list.append(each)
        print(f"add: {each}")
        time.sleep(.2)
    print(f'数据已添加完成: {pub_list}')

def read_proc():
    print(f"read: {pub_list}")

if __name__ == '__main__':
    add_process = mp.Process(target=add_proc)
    read_process = mp.Process(target=read_proc)
    add_process.start()

    # 主进程等待添加数据的进程执行完再往下执行
    add_process.join()
    read_process.start()
