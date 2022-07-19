#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/5/29
# @file 爬取微博图片.py
# -*- coding: utf-8 -*-
import os
import json
import time
import requests
import datetime
import urllib.request
from tqdm import trange
from random import choice

"""
# id = '6103252147'
# weibo_name = "我是狗头萝莉"

id = '5292770234'
weibo_name = 'Enndme'"""


def send_content(title, content):
    yag = yagmail.SMTP(user="leolswq@163.com", password="AVPBLRPCZTUXCYUS", host='smtp.163.com')
    yag.send('3181538941@qq.com', title, content)


path = 'D:\\weibo'
'''采集的站点：
    免费代理IP http://ip.yqie.com/ipproxy.htm
    66免费代理网 http://www.66ip.cn/
    89免费代理 http://www.89ip.cn/
    无忧代理 http://www.data5u.com/
    云代理 http://www.ip3366.net/
    快代理 https://www.kuaidaili.com/free/
    极速专享代理 http://www.superfastip.com/
    HTTP代理IP https://www.xicidaili.com/wt/
    小舒代理 http://www.xsdaili.com
    西拉免费代理IP http://www.xiladaili.com/
    小幻HTTP代理 https://ip.ihuan.me/
    全网代理IP http://www.goubanjia.com/
    飞龙代理IP http://www.feilongip.com/
'''
# 代理
proxy_addr = "122.241.72.191:808"

id = input("请输入要爬取的微博ID: ")
weibo_name = ''

proxy_addr_list = ['122.241.72.191:808', '47.101.44.122:80',
                   '116.63.93.172:8081', '42.180.208.43:8070',
                   '60.255.151.82:80', '218.2.214.107:80',
                   '116.117.134.135:9999', '202.108.22.5:80',
                   '45.64.22.24:80', '180.97.34.35:80',
                   '112.80.248.73:80', '116.117.134.135:8828',
                   '47.92.234.75:80', '203.74.120.79:3128',
                   '60.255.151.81:80', '39.106.223.134:80',
                   '222.74.202.229:80', '58.240.52.114:80']

pic_num = 0


def use_proxy(url, proxy_addr):
    req = urllib.request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    # 创建代理处理器
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    # 创建代理opener
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    # 安装opener
    urllib.request.install_opener(opener)
    # 发送请求
    data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    return data


# 获取容器编号
def get_containerid(url):
    containerid = ''
    data = use_proxy(url, proxy_addr)
    content = json.loads(data).get('data')
    for data in content.get('tabsInfo').get('tabs'):
        if data.get('tab_type') == 'weibo':
            containerid = data.get('containerid')
    return containerid


# 获取用户信息
def get_userInfo(id):
    global weibo_name
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id
    data = use_proxy(url, proxy_addr)
    content = json.loads(data).get('data')
    profile_image_url = content.get('userInfo').get('profile_image_url')
    description = content.get('userInfo').get('description')
    profile_url = content.get('userInfo').get('profile_url')
    verified = content.get('userInfo').get('verified')
    guanzhu = content.get('userInfo').get('follow_count')
    name = content.get('userInfo').get('screen_name')
    fensi = content.get('userInfo').get('followers_count')
    gender = content.get('userInfo').get('gender')
    urank = content.get('userInfo').get('urank')
    print("微博昵称：" + name + "\n" + "微博主页地址：" + profile_url + "\n" + "微博头像地址：" + profile_image_url + "\n" + "是否认证：" + str(
        verified) + "\n" + "微博说明：" + description + "\n" + "关注人数：" + str(guanzhu) + "\n" + "粉丝数：" + str(
        fensi) + "\n" + "性别：" + gender + "\n" + "微博等级：" + str(urank) + "\n")
    return name


# 核心逻辑, 爬取图片
def get_weibo(id, file):
    global pic_num
    i = 1
    while True:
        url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id
        weibo_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id + '&containerid=' + get_containerid(
            url) + '&page=' + str(i)
        try:
            data = use_proxy(weibo_url, proxy_addr)
            content = json.loads(data).get('data')
            cards = content.get('cards')
            if len(cards) > 0:
                for j in range(len(cards)):
                    print("-----正在爬取第" + str(i) + "页，第" + str(j) + "条微博------")
                    card_type = cards[j].get('card_type')
                    if card_type == 9:
                        mblog = cards[j].get('mblog')
                        attitudes_count = mblog.get('attitudes_count')
                        comments_count = mblog.get('comments_count')
                        created_at = mblog.get('created_at')
                        reposts_count = mblog.get('reposts_count')
                        scheme = cards[j].get('scheme')
                        text = mblog.get('text')
                        if mblog.get('pics') is not None:
                            # print(mblog.get('original_pic'))
                            # print(mblog.get('pics'))
                            pic_archive = mblog.get('pics')
                            for _ in range(len(pic_archive)):
                                pic_num += 1
                                print(pic_archive[_]['large']['url'])
                                img_url = pic_archive[_]['large']['url']
                                img = requests.get(img_url)
                                f = open(path + weibo_name + '\\' + str(pic_num) + str(img_url[-4:]),
                                         'ab')  # 存储图片，多媒体文件需要参数b（二进制文件）
                                f.write(img.content)  # 多媒体存储content
                                f.close()

                        with open(file, 'a', encoding='utf-8') as fh:
                            fh.write("----第" + str(i) + "页，第" + str(j) + "条微博----" + "\n")
                            fh.write("微博地址：" + str(scheme) + "\n" + "发布时间：" + str(
                                created_at) + "\n" + "微博内容：" + text + "\n" + "点赞数：" + str(
                                attitudes_count) + "\n" + "评论数：" + str(comments_count) + "\n" + "转发数：" + str(
                                reposts_count) + "\n" + '对应图片截至序号: ' + str(pic_num) + '\n')
                i += 1
            else:
                break
        except Exception as e:
            print(e)


def change_proxy():
    global proxy_addr, proxy_addr_list
    proxy_addr = choice(proxy_addr_list)


def get_weibo2(id, file):
    global pic_num
    i = 1
    exceptList = ['4578083913597712', '4784009710146164', '4782955979607266', '4784292493792481']
    while True:
        # change_proxy()
        url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id
        weibo_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id + '&containerid=' + get_containerid(
            url) + '&page=' + str(i)
        try:
            data = use_proxy(weibo_url, proxy_addr)
            content = json.loads(data).get('data')
            cards = content.get('cards')
            # if (len(cards) > 0):
            for j in range(3):
                # print("-----正在爬取第" + str(i) + "页，第" + str(j) + "条微博------")
                card_type = cards[j].get('card_type')
                if card_type == 9:
                    mblog = cards[j].get('mblog')
                    attitudes_count = mblog.get('attitudes_count')
                    comments_count = mblog.get('comments_count')
                    created_at = mblog.get('created_at')
                    reposts_count = mblog.get('reposts_count')
                    scheme = cards[j].get('scheme')
                    text = mblog.get('text')
                    if (_id := mblog.get('id')) in exceptList:
                        # print('pass ', _id)
                        continue
                    else:
                        exceptList.append(_id)
                        content = '微博内容: ' + text + '微博地址: ' + scheme
                        send_content('微博更新', content)
                        print("append: ", _id)
                        print(content)
                    if mblog.get('pics') is not None:
                        # print(mblog.get('original_pic'))
                        # print(mblog.get('pics'))
                        pic_archive = mblog.get('pics')
                        for _ in range(len(pic_archive)):
                            pic_num += 1
                            print(pic_archive[_]['large']['url'])
                            imgurl = pic_archive[_]['large']['url']
                            img = requests.get(imgurl)
                            f = open(path + weibo_name + '\\' + str(pic_num) + str(imgurl[-4:]),
                                     'ab')  # 存储图片，多媒体文件需要参数b（二进制文件）
                            f.write(img.content)  # 多媒体存储content
                            f.close()

                    with open(file, 'a', encoding='utf-8') as fh:
                        fh.write("----第" + str(i) + "页，第" + str(j) + "条微博----" + "\n")
                        fh.write("微博地址：" + str(scheme) + "\n" + "发布时间：" + str(
                            created_at) + "\n" + "微博内容：" + text + "\n" + "点赞数：" + str(
                            attitudes_count) + "\n" + "评论数：" + str(comments_count) + "\n" + "转发数：" + str(
                            reposts_count) + "\n" + '对应图片序号: ' + str(pic_num) + '\n')
                # i += 1
            print('\r', end='')
            for _ in 'wait for the image':
                print(_, end='')
                time.sleep(1)

            # break
        except Exception as e:
            print(e)
            pass


if __name__ == "__main__":
    # 1749127163
    # 获取基本信息
    weibo_name = get_userInfo(id)
    # 初始化准备
    if not os.path.isdir(path + weibo_name):
        os.mkdir(path + weibo_name)
    file = path + weibo_name + '\\' + weibo_name + ".txt"
    get_weibo(id, file)

    # # 定时开始
    # goal_time = datetime.time(16, 53, )
    # while True:
    #     if datetime.datetime.now().time() > goal_time:
    #         txt = f"{'$' * 10} begin {'$' * 10} \n at: {datetime.datetime.now()}"
    #         print(txt)
    #         with open(file, 'w') as f:
    #             f.write(txt)
    #         break

    # 爬取完成, 发送邮件
    send_content(
        f"爬取完成",
        f"{weibo_name}微博的图片爬取完成, 共爬取{pic_num}张图片"
    )
