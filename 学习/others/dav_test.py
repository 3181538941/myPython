#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from webdav4.client import Client
import os

options = {
    'base_url': 'https://pan.i95cloud.com/dav',
    'auth'    : ('3181538941@qq.com', 'm3xpIuRx8fJKJiBGdXVtqV9EAu66b9rM')
}

client = Client(**options)


def upload(path):
    """

    :type path: str
    """
    homeList = os.listdir(path)

    for item in homeList:
        if os.path.isfile(item):
            try:
                from_path: str = os.path.join(path, item)
                client.upload_file(from_path=from_path, to_path=f'{item}', overwrite=True)
                print(f'success upload {item}')
            except:
                print(f'file to upload {path}{item}')
        # if os.path.isdir(item) and item not in excepts:
        #     upload(item)


upload('./')
print('-----complete deal files-----')

# client.upload_file(from_path="./jianguo.py",to_path="/dav_test.py")
# client.upload_file(from_path='./Email.py', to_path='/Email.py', overwrite=False)
# client.download_file(from_path='/Email.py', to_path='./test/dav1.py', )
# a = client.isfile('/dav.py')
# print(a)
#
# s = client.ls(path="/", detail=False)
# print(s)

"""
其他操作: 
    download_file : 下载文件到本地
    move ：移动
    copy ：复制
    remove ：移除
    mkdir ： 创建文件夹
    exists ：检查给出的资源路径是否存在
    isdir ：检查是否是文件夹t
    isfile ：是否是文件
"""
