#!/usr/bin/env python3
# -*- coding" = "utf-8 -*-
# @author LeoWang
# @date 2022/6/21
# @file req.py
import requests
import json
from http import cookiejar


def login():
    login_url = 'https://10-2-0-102.sslvpn.beihua.edu.cn/jsxsd/xk/LoginToXk'
    head = {
        'Accept'         : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control'  : 'max-age=0',
        'Connection'     : 'keep-alive',
        'Content-Type'   : 'application/x-www-form-urlencoded',
        'Cookie'         : 'JSESSIONID=43F827962C4BD4E7998D41DEBF0D5FA9; iPlanetDirectoryPro=YTtQTT1QAmS04I1H1AVQz1; SERVERID=121; JSESSIONID=A6CBB40BB5BDA8D3ABD257AA1607D0E7; _webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMjAyMDE1MDIwNDI2IiwiZ3JvdXBzIjpbMV0sImlhdCI6MTY1NTc2NTEwNCwiZXhwIjoxNjU1ODUxNTA0fQ.e3sBfGw2zskWv7nLpoBe1zUcFdzpXzjJtKHQGJOKXYk; webvpn_username=202015020426%7C1655765104%7Cc112fb773a00b1c21906bf124481313efbece390',
        'Host'           : '10-2-0-102.sslvpn.beihua.edu.cn',
        'Origin'         : 'https://10-2-0-102.sslvpn.beihua.edu.cn',
        'Referer'        : 'https://10-2-0-102.sslvpn.beihua.edu.cn/jsxsd/'
    }
    data = {
        'loginMethod' : 'LoginToXk',
        'userAccount' : '202015020426',
        'userPassword': '3181538941as',
        'encoded'     : 'MjAyMDE1MDIwNDI2%25%25%25MzE4MTUzODk0MWFz'
    }
    r = requests.post(login_url, headers=head, data=data)
    print(r.text)


def getTable():
    url = "https://10-2-0-102.sslvpn.beihua.edu.cn/jsxsd/pyfa/topyfamx"
    head = {
        'Accept'         : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection"     : "keep-alive",
        "Cookie"         : "JSESSIONID=43F827962C4BD4E7998D41DEBF0D5FA9; iPlanetDirectoryPro=YTtQTT1QAmS04I1H1AVQz1; SERVERID=121; JSESSIONID=A6CBB40BB5BDA8D3ABD257AA1607D0E7; _webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMjAyMDE1MDIwNDI2IiwiZ3JvdXBzIjpbMV0sImlhdCI6MTY1NTc2NjQwOSwiZXhwIjoxNjU1ODUyODA5fQ.9fWR4NR9nPc72lBE7jD7O4-WPCD8TAo-1UGX2HSsGlQ; webvpn_username=202015020426%7C1655766409%7C616374ea4106b2671dfd5ef0a1384998f8512161;Host: 10-2-0-102.sslvpn.beihua.edu.cn",
        "Referer"        : "https://10-2-0-102.sslvpn.beihua.edu.cn/jsxsd/framework/xsMainV.htmlx"
    }
    cookies = {
        'JSESSIONID':
    'KrODt3ZeIGljDumqaUSC5H6hF3NIvGeRPt88DBW_kYzIlLbmN2qU!1917689344',
        'SERVERID':    'Server1',
        '_astraeus_session': 'UEUwRkQ2WFh2M0JicDlZMDRnQlQ4OHVVaFRxVWhnME9Oa0lVMEpPbVpJV0Z2OWQ3QXEwSFhRNFc4a3pkVGloRE9YNS8yN2hJa3BoekhrT0VlWU84QXlVdkJUNjRtZkVraDdEWnhFU0gwc01rYVhmSFdYWHdzVWVuOHN3YlkvWDMwaTRMWDB4U0NsTHNPL2h2a3FsT1hOYUxmQ3poNFF4QWlTVnIzYlBYVEEwMkZPSFVVOXJ2cmIrZEp2bldsWW9XRjdJaDdZaVUwMEptTi94OE4wREtUZkNnOVJQb2NBQjU5RDlCTm44a2liQkR6aHJjZUpFYXhkV1NLeW1IbnVpdi0tajFOL0NMTlBscGRML0JmQm4xNkFxUT09',
        'route':'10513848484348d0b7c3e5f025a26a4d,'
                'JSESSIONID'
    }
    req = requests.get(url, headers=head)
    print(req.text)


def test():
    filename = r'A:\a.data\test\.idea\httpRequests\http-client.cookies'
    # 创建MozillaCookieJar实例对象
    cookie = cookiejar.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    cookie.load(filename, ignore_discard=True, ignore_expires=True)
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler = request.HTTPCookieProcessor(cookie)
    print(handler)
    print(cookie)

    # 通过CookieHandler创建opener
    opener = request.build_opener(handler)
    print(opener)
    # 此用opener的open方法打开网页
    # response = opener.open('http://www.baidu.com')


if __name__ == '__main__':
    # login()
    getTable()
    # test()