#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/2/22
# @file 文件传输_服务端.py
import socket

# 创建 socket 对象, 使用 TCP协议
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置套接字地址可以重用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 绑定 IP 端口
address = ("", 8081)
tcp_server_socket.bind(address)
# 开启监听
# listen方法设置该套接字为被动监听模式, 不能主动发送数据
# 128: 允许最大连接数
tcp_server_socket.listen(128)
# 等待客户端连接,
# accept方法返回值为(新的套接字,(客户端IP, 端口))
new_client_socket, client_ip_port = tcp_server_socket.accept()
print(client_ip_port)
# 接收信息(也可发送信息)
file = new_client_socket.recv(1024)
print(file.decode('utf-8'))

with open(file, 'rb') as f:
    f.seek(0)
    while True:
        per_data = f.read(1024)
        if not per_data:
            break
        new_client_socket.send(per_data)
# 关闭套接字, 不和此客户端通信
new_client_socket.close()

# 关闭服务器套接字, 不再和新的客户端建立连接, 已连接的可以继续服务
tcp_server_socket.close()
