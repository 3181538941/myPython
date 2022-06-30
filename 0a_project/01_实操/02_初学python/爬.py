#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2021/1/12
# @file 爬.py

# 爬虫爬取网址https://www.mzitu.com/zipai/上的图片
import urllib.request
import os


def url_open(url):
    req = urllib.request.Request(url)
    # 添加头部，伪装Goole浏览器
    req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    return html


# 得到页数
def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('page-numbers current') + 22  # +22是从字符‘p’到页数共偏移22个字符，下同
    b = html.find('<', a)

    return html[a:b]


# 得到图片地址
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('data-original=')
    while a != -1:
        b = html.find('.jpg', a, a + 255)
        if b != -1:
            img_addrs.append(html[a + 15:b + 4])  # +15，+4同样是偏移字符的个数
        else:
            b = a + 22
        a = html.find('data-original=', b)
    # 打印图片地址
    # for each in img_addrs:
    #    print(each)
    return img_addrs


# 保存图片
def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)


def download_mm_img(folder, pages):
    os.mkdir(folder)
    os.chdir(folder)

    url = "https://www.mzitu.com/zipai/"
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'comment-page-' + str(page_num) + '/#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)
    print("抓取成功！")


if __name__ == '__main__':
    pages_num = input("请输入要抓取的图片页数：")
    pages_num = int(pages_num)
    file_name = input("请输入要保存的文件名称：")
    download_mm_img(file_name, pages_num)