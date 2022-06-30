#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/2/26
# @file 服务器_返回固定页面.py
import socket


def request_handler(new_socket, ip_port):
    # 接收信息(也可发送信息)
    rec = new_socket.recv(1024)
    print(rec.decode('utf-8'))

    # 协议判空
    if not rec:
        print(f'{ip_port} 客户端已下线')
        # 关闭套接字, 不和此客户端通信
        new_socket.close()
        return

    # 响应报文
    response = '''HTTP/1.1 200 OK
Server: leoPyServer1.0''' + '\r\n'

    # 读取并返回文件
    with open(r'.\个人简介.html', 'r', encoding='utf-8') as html:
        response_body = html.read()

    response += response_body

    new_socket.send(response.encode('utf-8'))
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
    address = ("", 31813)
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
