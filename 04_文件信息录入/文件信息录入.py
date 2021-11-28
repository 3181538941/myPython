# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2021/3/24
# @file 文件信息录入.py

# import pickle
# import os

file_dat = ''  # type: str
dat_temp = ''  # type: str

def read_file():
    global file_dat
    with open('data.dat', 'rb') as file:
        file_dat = file.read()
    print '\n读取成功\n'
    if file_dat == '0':
        print '但文件内没有内容'
    # for each in file:
    #     file_dat=each
    # 整体读取(pickle)
    # global file_dat
    # with open('data.dat', 'rb') as file:
    #     file_dat = pickle.load(file)


def save_file(dat):
    with open('data.dat', 'ab') as file:
        for each in dat:
            file.write(each)
    print '保存成功'
    # 整体保存(pickle)
    # with open('data.dat', 'ab') as file:
    #     pickle.dump(dat, file)


def inputvalue():
    global dat_temp
    print '请输入想要录入的信息'
    dat_temp = str(raw_input())


def clear_file():
    with open('data.dat', 'wb') as temp:
        temp.write('0')
    print '清除成功'


def print_file(dat):
    if dat == '0':
        print '\n<!--文件内无内容-->'
    else:
        print dat


def menu():
    print '''
    请选择想使用的功能:
        0.退出程序;
        1.从文件中读取信息;
        2.显示刚读取的信息;
        3.输入信息;
        4.显示刚录入的信息;
        5.保存刚录入的信息;
        6.清空信息;
        '''
    a = int(input())
    return a


while 1:
    choice = menu()
    if choice == 0:    # 退出程序
        break
    elif choice == 1:  # 读取信息
        read_file()
    elif choice == 2:  # 显示信息
        print_file(file_dat)
    elif choice == 3:  # 输入信息
        inputvalue()
    elif choice == 4:  # 显示刚录入的信息
        print_file(dat_temp)
    elif choice == 5:  # 保存刚录入的信息
        save_file(dat_temp)
    elif choice == 6:  # 清空信息
        clear_file()

# save(file_dat)
# print file_dat
# inputValue()
