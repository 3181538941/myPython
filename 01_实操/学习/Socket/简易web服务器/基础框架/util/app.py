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


def application(request, fu_path):
    """根据客户端请求的路径返回资源"""

    # 解析报文, 得到请求路径
    file_path = parse_request(request)

    if file_path == '/':
        # 默认返回页面
        response = 'HTTP/1.1 200 OK\r\n' + 'Server: leoPyServer1.0\r\n' + '\r\n'
        response += '<h1>Hello World</h1>'
        response = response.encode('utf-8')
    elif os.path.isfile(fr'{fu_path}{file_path}'):
        # 响应报文
        response = 'HTTP/1.1 200 OK\r\n' + 'Server: leoPyServer1.0\r\n' + '\r\n'

        with open(fr'{fu_path}{file_path}', 'rb') as html:
            response_body = html.read()
        response = response.encode('utf-8')
        response += response_body

    else:
        response = 'HTTP/1.1 404 Not Found\r\n' + 'Server: leoPyServer1.0\r\n' + '\r\n'
        response = response.encode('utf-8')
    return response
