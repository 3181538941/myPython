#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2021/3/24
# @file 文件信息录入.py

# import pickle
import os


def read():
    global file_dat
    with open('data.dat', 'rb') as file:
        file_dat = file.read()
        # for each in file:
        #     file_dat=each
    # 整体读取(pickle)
    # global file_dat
    # with open('data.dat', 'rb') as file:
    #     file_dat = pickle.load(file)


def save(dat):
    with open('data.dat', 'wb') as file:
        for each in dat:
            file.write(each)
    # 整体保存(pickle)
    # with open('data.dat', 'ab') as file:
    #     pickle.dump(dat, file)


def inputValue():
    i = os.system('cls')
    print
    '请输入想要录入的信息'


def menu():
    print
    '''
       请选择想使用的功能:
           0.退出程序
           1.输入信息;
           2.保存信息;
           3.读取信息;
           4.清空信息;
           '''
    choice = int(input())
    return choice
    # i = os.system('cls')


file_dat = '121'
# while 1:
#     if menu() == 0:
#         break
#     elif menu() == 1:
#         pass

read()
# save(file_dat)
print
file_dat
inputValue()
i = os.system("cls")
