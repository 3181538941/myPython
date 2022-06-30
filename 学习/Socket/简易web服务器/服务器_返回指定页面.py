#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/2/26
# @file 服务器_返回指定页面.py
import socket
import os
from urllib.parse import unquote


def request_handler(new_socket, ip_port):
    # 接收信息
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

    # 根据客户端请求的路径返回资源
    rec_data = unquote(rec)
    rec_head = rec_data[:rec_data.find('\r\n')]
    rec_list = rec_head.split()
    file_path = rec_list[1]

    # 响应报文
    response = 'HTTP/1.1 200 OK\r\n' + 'Server: leoPyServer1.0\r\n' + '\r\n'

    # 默认返回页面
    if file_path == '/':
        response = 'HTTP/1.1 200 OK\r\n' + 'Server: leoPyServer1.0\r\n' + '\r\n'
        response += '<h1>Hello World</h1>'
        response = response.encode('utf-8')
    elif os.path.isfile(fr'个人主页{file_path}'):
        with open(fr'个人主页{file_path}', 'rb') as html:
            response_body = html.read()

        response = response.encode('utf-8')
        response += response_body

    else:
        response = 'HTTP/1.1 404 Not Found\r\n' + 'Server: leoPyServer1.0\r\n' + '\r\n'
        response = response.encode('utf-8')

    new_socket.send(response)
    # 关闭套接字, 不和此客户端通信
    new_socket.close()


if __name__ == '__main__':
    """
    接收信息, 做出响应
    :return:
    """

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
    while True:
        # accept方法返回值为(新的套接字,(客户端IP, 端口))
        new_client_socket, client_ip_port = tcp_server_socket.accept()
        request_handler(new_client_socket, client_ip_port)

    # # 关闭服务器套接字, 不再和新的客户端建立连接, 已连接的可以继续服务
    # tcp_server_socket.close()
