#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/3/6
# @file 02_给进程传参.py
import multiprocessing as mp

def show_info(name, arg):
    print(name, arg)



if __name__ == '__main__':
    # 以元组形式传参
    # sub_process = mp.Process(target=show_info, args=('测试',31814))
    # 以字典形式传参
    sub_process = mp.Process(target=show_info, kwargs={'name':"测试",'arg':31814})
    sub_process.start()