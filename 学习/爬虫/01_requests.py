#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/3/12
# @file 01_requests.py
import requests

url = 'https://www.upyunso.com/'

res = requests.get(url)

# 相应结果
print(res)
# 状态码
print(res.status_code)
# 二进制文本流
# print(res.content)
# 二进制文本流装成字符串
# print(res.content.decode('utf-8'))
# 响应内容
print(res.text)
# 请求的地址
print(res.url)
# 请求头信息
print(res.request.headers)
# 响应头信息
print(res.headers)
