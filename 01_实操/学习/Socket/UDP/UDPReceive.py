#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/2/21
# @file UDPReceive.py
import socket
import time
# 创建 socket 对象, 使用 IPv4, UDP协议
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 创建 socket 对象, 使用 TCP协议
# tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定端口
add_ = ('',8081)
udp_socket.bind(add_)

# 接收数据
rec = udp_socket.recvfrom(1024)
# print(rec)
print(rec[0].decode(encoding='utf-8'))
print(rec[1])
# 关闭套接字
udp_socket.close()
# tcp_soc.close()


