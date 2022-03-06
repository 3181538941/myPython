#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/2/27
# @file 服务器_基础框架构建.py
import socket
import sys
from urllib.parse import unquote
from util import application

class WebServer(object):

    def __init__(self):
        # 创建 socket 对象, 使用 TCP协议
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置套接字地址可以重用
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定 IP 端口
        address = ("", self.getHost())
        self.tcp_server_socket.bind(address)
        # 开启监听
        # listen方法设置该套接字为被动监听模式, 不能主动发送数据
        # 128: 允许最大连接数
        self.tcp_server_socket.listen(128)

    def getHost(self):
        host = 8080
        if len(sys.argv) > 1:
            if sys.argv[1].isdigit():
                host = int(sys.argv[1])
        else:
            print(f"参数错误或未附带参数, 使用默认端口{host}")
        return host


    def request_handler(self, new_socket, ip_port):
        """
        接收信息, 做出响应
        """
        rec = new_socket.recv(1024)
        # 使用 unquote 进行url解码
        print(unquote(rec))
        # print(rec.decode('utf-8'))

        # 协议判空
        if not rec:
            print(f'{ip_port} 客户端已下线')
            # 关闭套接字, 不和此客户端通信
            new_socket.close()
            return

        response = application(rec, '../个人主页')

        new_socket.send(response)
        # 关闭套接字, 不和此客户端通信
        new_socket.close()

    def start(self):
        """启动Web服务器"""
        # 等待客户端连接,
        while True:
            # accept方法返回值为(新的套接字,(客户端IP, 端口))
            new_client_socket, client_ip_port = self.tcp_server_socket.accept()
            self.request_handler(new_client_socket, client_ip_port)

        # # 关闭服务器套接字, 不再和新的客户端建立连接, 已连接的可以继续服务
        # self.tcp_server_socket.close()

if __name__ == '__main__':
    server = WebServer()
    server.start()
