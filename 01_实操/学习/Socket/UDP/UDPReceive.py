#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/2/21
# @file UDPReceive.py
import socket
# 创建 socket 对象, 使用 IPv4, UDP协议
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
udp_socket.bind(('',8082))

# 接收数据
rec = udp_socket.recvfrom(1024)
# print(rec)
print(rec[0].decode(encoding='utf-8'))
print(rec[1])
# 关闭套接字
udp_socket.close()
# tcp_soc.close()


