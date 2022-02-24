#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/2/22
# @file TCP客户端.py

import socket
# 创建 socket 对象, 使用 TCP协议
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
address = ("192.168.31.125",8081)
tcp_client.connect(address)
# 发送信息(也可接收信息)
while 1:
    msg = input()
    if msg:
        tcp_client.send(msg.encode('utf-8'))
    else:
        break


# 关闭套接字
tcp_client.close()


