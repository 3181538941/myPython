#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/2/27
# @file app.py.py
from urllib.parse import unquote
import os


def parse_request(request):
    """解析请求, 返回资源路径"""
    rec_data = unquote(request)  # 将报文进行解码
    rec_head = rec_data[:rec_data.find('\r\n')]
    rec_list = rec_head.split()
    return rec_list[1]


def application(request, father_path):
    """根据客户端请求的路径返回资源"""

    # 解析报文, 得到请求路径
    file_path = father_path + parse_request(request)

    if file_path == f'{father_path}/':
        # 默认返回页面
        response = 'HTTP/1.1 200 OK\r\n' + 'Server: leoPyServer1.0\r\n' + '\r\n'
        response += '<h1>Welcome to Leo\'s Server</h1><h2>Wait to Build</h2>'
        response = response.encode('utf-8')
    elif os.path.isfile(file_path):
        # 响应报文
        response = 'HTTP/1.1 200 OK\r\n' + 'Server: leoPyServer1.0\r\n' + '\r\n'
        response = response.encode('utf-8')
        # 发送客户端请求文件, 以二进制形式读取文件, 利于发送图片
        with open(file_path, 'rb') as html:
            response_body = html.read()
        response += response_body

    else:
        response = 'HTTP/1.1 404 Not Found\r\n' + 'Server: leoPyServer1.0\r\n' + '\r\n'
        response = response.encode('utf-8')
    return response

if __name__ == '__main__':

    import sys
    print(sys.argv)