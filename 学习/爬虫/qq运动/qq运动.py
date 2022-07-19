#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/7/16
# @file qq运动.py
import requests
import re
import time

url = 'https://yundong.qq.com:443/v2/rank/friend?_wv=18950113&_wwv=8192'
cookie = {
    'gdt_device_info_h5': 'eyJhaWRfdGlja2V0IjoiMDE5MEM2REJEMzY1RTdDRUM1QzkxNUM0MEJFQTFCOEEwODYwMUQ0Q0IwMDZEQTRFNjYiLCJhcHBfdmVyc2lvbl9pZCI6NTM3MDY2NDE5LCJicmFuZCI6IlhpYW9taSIsImNhcnJpZXJfY29kZSI6NDYwMDEsImNsaWVudF9pcHY0IjoiMTM5LjIxMC4xNzAuOTgiLCJjb25uIjoxLCJkZXZpY2VfYnJhbmRfYW5kX21vZGVsIjoiTTIxMDJLMUMiLCJkZXZpY2VfZXh0Ijoie1wid2VjaGF0X2luc3RhbGxlZF9pbmZvXCI6e1wiaGFzX3VuaXZlcnNhbF9saW5rXCI6ZmFsc2UsXCJhcGlfdmVyXCI6XCI2NzEwOTQ1ODJcIixcImluc3RhbGxlZFwiOmZhbHNlfSxcImF0dHJpX2luZm9cIjp7XCJ3bV9oXCI6XCJjODA4NjkwMjAxMmY5N2Q0YmJiNjMyMWJjZmIxY2QzOVwiLFwidWFcIjpcIkRhbHZpa1xcLzIuMS4wIChMaW51eDsgVTsgQW5kcm9pZCAxMjsgTTIxMDJLMUMgQnVpbGRcXC9TS1ExLjIyMDMwMy4wMDEpXCJ9LFwibXFxX2NvbmZpZ19zdGF0dXNcIjoxLFwiYXBwX3N0YXR1c1wiOnt9LFwicWFpZF9pbmZvXCI6e319IiwiaXNfZ29vZ2xlcGxheV92ZXJzaW9uIjpmYWxzZSwibG9jYXRpb24iOnsiY29vcmRpbmF0ZXNfdHlwZSI6MCwibGF0aXR1ZGUiOjQ0NjgwNTQzLCJsb25naXR1ZGUiOjEyNjY3NDcyN30sIm1hbnVmYWN0dXJlciI6IlhpYW9taSIsIm1kNV9hbmRyb2lkX2lkIjoiMWU0YTFiMDNkMWI2Y2Q4YTE3NGE4MjZmNzZlMDA5ZjQiLCJtdWlkX3R5cGUiOjAsIm9yaWdpbl9uZXR3b3JrX3R5cGUiOjEwLCJvc190eXBlIjoyLCJvc192ZXIiOiIxMiIsInFxX3ZlciI6IjguNC4xOCIsInRhaWRfdGlja2V0IjoiMDEwMTg2OUY2MzI4RkY0QUVBOENBMzVEQzFBQTVBMEQyN0ZFMzJERDAxNjhGODgwNkIxNTBGRTE5NDlBM0QyNzNGNjM4RTM4OTgwRDRCQzVBREY0MURGNiJ9',
    'qq_locale_id'      : '2052',
    'uin'               : 'o3181538941',
    'p_uin'             : 'o3181538941',
    'p_skey'            : 'AbikNC13-uW9OBEmMMi-8LuRzyVgpUkRsSK1WOshr6s_',
    'skey'              : 'M0kOExB5ND',
    'qv_als'            : 'R2YFCzlMdbbi1ThzA11657935032+PZZig::',
    'xClientProtoVer'   : 'https_http2'
}
head = {
    'User-Agent'      : 'Mozilla/5.0 (Linux; Android 12; M2102K1C Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 V1_AND_SQ_8.4.18_1558_YYB_D A_8041800 QQ/8.4.18.4945 NetType/3G WebP/0.4.1 Pixel/1440 StatusBarHeight/138 SimpleUISwitch/1 QQTheme/2921 InMagicWin/0',

    'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'X-Requested-With': 'com.tencent.mobileqq',
    'Accept-Encoding' : 'gzip, deflate',
    'Accept-Language' : 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}
res = requests.get(url, headers=head, cookies=cookie)
with open(f"rec_{time.strftime('%m_%d_%H_%M')}.html", 'w', encoding='utf-8') as f:
    f.write(res.text)
