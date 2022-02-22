#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/2/20
# @file UDPSend.py
import socket
# 创建 socket 对象, 使用 IPv4, UDP协议
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定 IP 端口
add_ = ("192.168.31.125",8080)
udp_socket.bind(add_)

# 发送UDP消息
udp_socket.sendto("hello".encode(encoding='utf-8'),("192.168.31.136",8081))
def sendBroadcast(msg,ip,host,coding='utf-8'):
    # 设置广播权限
    # udp_socket.setsockopt(套接字, 属性, 属性值)
    # socket.SOL_SOCKET: 当前的套接字
    # socket.SO_BROADCAST: 广播属性
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    # 发送信息
    udp_socket.sendto(msg.encode(encoding=coding),(ip,host))

# 发送UDP广播
sendBroadcast('test of broadcast','255.255.255.255',8081)

# 关闭套接字
udp_socket.close()