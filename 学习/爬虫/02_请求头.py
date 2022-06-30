#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/3/12
# @file 02_请求头.py
import requests

url = 'https://www.kuaidaili.com/free/inha/'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36"
}

res = requests.get(url,headers=headers)


print(res.status_code)