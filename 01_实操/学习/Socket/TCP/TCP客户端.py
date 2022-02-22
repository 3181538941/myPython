#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/2/22
# @file TCP客户端.py

import socket
# 创建 socket 对象, 使用 TCP协议
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
address = ("192.168.31.125",8082)
tcp_client.connect(address)


tcp_client.send('test'.encode('utf-8'))

# rec_data = tcp_client.recv(1024)
# print(rec_data)


# 关闭套接字
tcp_client.close()


