#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/2/22
# @file 文件传输_客户端.py


import socket

# 创建 socket 对象, 使用 TCP协议
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
address = ("192.168.31.125", 8081)
tcp_client.connect(address)
# 发送要下载的文件名
# D:\林深雾起\OneDrive\图片\terminal.ico
# D:\Video\Captures\赘婿-第12集在线播放-2021-03-02 20-25-00.mp4
file_name = input("请输入要下载的文件: ")
tcp_client.send(file_name.encode('utf-8'))
with open('test.ico', 'wb') as f:
    while True:
        per_data = tcp_client.recv(1024)
        if not per_data:
            break
        f.write(per_data)

# 关闭套接字
tcp_client.close()
