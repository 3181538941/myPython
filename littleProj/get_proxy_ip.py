#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/6/25
# @file get_proxy_ip.py
import requests

url = 'http://ip.yqie.com/ipproxy.htm'

a = requests.get(url)

print(a.content)

print(a.text)
