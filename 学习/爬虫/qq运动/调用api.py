#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/7/16
# @file 调用api.py
import requests

url = "https://yundong.qq.com:443/pushsport/cgi/rank/friends?g_tk=1854012578"
# 请求体
dcapiBody = {
    'dcapiKey': 'user_rank',
    'l5apiKey': 'rank_friends',
    'params'  : {
        "cmd": 1, "pno": 3, "dtype": 1, "pnum": 20
    }
}
Cookie = {
    'qq_locale_id'   : '2052',
    'uin'            : 'o3181538941',
    'p_uin'          : 'o3181538941',
    'p_skey'         : 'AbikNC13-uW9OBEmMMi-8LuRzyVgpUkRsSK1WOshr6s_',
    'skey'           : 'M0kOExB5ND',
    'qv_als'         : 'R2YFCzlMdbbi1ThzA11657935032+PZZig==',
    'xClientProtoVer': 'https_https1'
}

head = {
    'Accept'          : 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent'      : 'Mozilla/5.0 (Linux; Android 12; M2102K1C Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 V1_AND_SQ_8.4.18_1558_YYB_D A_8041800 QQ/8.4.18.4945 NetType/WIFI WebP/0.4.1 Pixel/1440 StatusBarHeight/138 SimpleUISwitch/1 QQTheme/2921 InMagicWin/0',
    'Content-Type'    : 'application/x-www-form-urlencoded',
    'Accept-Encoding' : 'gzip, deflate',
    'Accept-Language' : 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}

req = requests.post(url, data=dcapiBody, cookies=Cookie, headers=head)
print(req.text)
