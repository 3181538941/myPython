#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/5/8
# @file downloadEle.py
# encoding:utf-8
from bs4 import BeautifulSoup
import requests, re, os, socket
from urllib import request

# 指定要下载的版本
element_ui_version = "2.15.7"
# 指定文件要存放的位置
element_ui_dir = "D:/0a.dataout/test/tmp"

save_ui_dir = os.path.join(element_ui_dir, "element-ui")

if not os.path.isdir(save_ui_dir):
    os.makedirs(save_ui_dir)

element_ui_url = "https://unpkg.com/browse/element-ui@" + element_ui_version + "/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"
}


def get_page(url, save_dir):
    print("Current Page:    ", url)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(str(response.content), "lxml")
    tbody = soup.find("tbody")
    rule_name = r'href="(.+?)"'
    td_href = re.findall(rule_name, str(tbody))
    dir_list = []
    for href in td_href:
        href_path = os.path.join(save_dir, href)
        if href == "../":
            pass
        elif "/" in href:
            os.mkdir(href_path)
            print("Makedir:    ", href_path.replace(save_ui_dir, ""))
            dir_list.append(href)
        else:
            file_url = url + href
            abs_name = file_url.replace(element_ui_url, "")
            print("Download:    ", abs_name)
            get_file(file_url, href_path)

    for sub_dir in dir_list:
        sub_url = url + sub_dir
        sub_dir = os.path.join(save_dir, sub_dir)
        get_page(sub_url, sub_dir)


def get_file(url, filename):
    opener = request.build_opener()
    opener.addheaders = [('User-agent',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0')]
    request.install_opener(opener)
    socket.setdefaulttimeout(30)
    url = url.replace("browse/", "")
    count = 1
    while count <= 5:
        try:
            request.urlretrieve(url, filename)
            break
        except socket.timeout:
            err_info = '<Timeout>   Reloading for %d time' % count
            print(err_info)
            count += 1
        except Exception as e:
            err_info = '<' + str(e) + '>   Reloading for %d time' % count
            print(err_info)
            count += 1
    if count > 5:
        print("<Error>  download job failed!")
    else:
        pass


get_page(element_ui_url, save_ui_dir)
