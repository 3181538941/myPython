#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/3/12
# @file 03_post请求.py
import requests
from urllib.parse import unquote

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36",
}
# post发送的数据
data = {
    'kw': 'chinese'
}

url = rf'https://fanyi.baidu.com/sug'

res = requests.post(url, headers=headers, data=data)
content = res.json()
print(res.status_code)
print(content['data'][0]['k'])
print(content['data'][0]['v'].split(';')[0])