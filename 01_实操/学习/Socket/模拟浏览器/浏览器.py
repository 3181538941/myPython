#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/2/26
# @file 浏览器.py
import socket

# 创建套接字
browser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置套接字地址可以重用
browser.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

add_ = ('www.alipanso6.com', 80)
# browser.bind(add_)
# 建立连结
browser.connect(add_)
# 请求报文
# 请求行
request_line = "GET / HTTP/1.1\r\n"
# 请求头
request_head = "Host:www.alipanso6.com\r\n"
# 请求空行
request_blank = '\r\n'
# 字符串拼接
request_data = request_line + request_head + request_blank
# 发送请求
browser.send(request_data.encode('utf-8'))
# 接收服务器相应内容
recv_data = browser.recv(10240).decode('utf-8')
print(recv_data)
locate = recv_data.find('\r\n\r\n')
with open('index.html', 'w',encoding='utf-8') as html:
    html.write(recv_data[locate + 4:])
browser.close()
