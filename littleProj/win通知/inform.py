#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/6/23
# @file inform.py
from win10toast import ToastNotifier

toaster = ToastNotifier()


def icon_toast():
    # 有icon的版本, 调用后阻塞线程
    toaster.show_toast("Hello World!!!",
                       "Python is 5 seconds awsm!",
                       icon_path="main.ico",
                       duration=5)


def thread_toast():
    # 无icon，采用python的icon，且采用自己的线程, 多次调用只执行一次
    toaster.show_toast("Example two",
                       "This notification is in it's own thread!",
                       icon_path=None,
                       duration=5,
                       threaded=True)


# if toaster.notification_active():
# print(toaster.notification_active())
# 等待提示框关闭
# while toaster.notification_active():
#     time.sleep(0.1)

if __name__ == '__main__':
    icon_toast()
    icon_toast()
    icon_toast()
    icon_toast()
