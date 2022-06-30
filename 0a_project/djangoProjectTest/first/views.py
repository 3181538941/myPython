#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/4/23
# @file views.py.py
import os

from django.shortcuts import render
from django.http import HttpResponse
from djangoProjectTest import IMG_UPLOAD


def hello(request):
    return HttpResponse("Hello world leo")


def home(request):
    # 配置模板视图, 将模板中的 变量名leo 按字典替换
    context = {
        'leo'     : 'Hello leo!',
        'testList': [123, 456, 789]
    }
    print('request: ', request)
    print(request.FILES)
    return render(request, 'home.html', context)


# Create your views here.
def index(request):
    return render(request, 'index.html')


# /upload_action/
def upload_action(request):
    """保存上传文件"""
    # 1.获取上传的文件
    pic = request.FILES['pic']
    # 2.创建文件
    save_path = os.path.join(IMG_UPLOAD, pic.name)
    with open(save_path, 'wb') as f:
        # 获取上传文件的内容并写到创建文件中
        # pic.chunks():分块的返回文件
        for content in pic.chunks():
            f.write(content)
    # # 3.将保存操作写到数据库中
    # PicTest.objects.create(gpic='booktest/%s' % pic.name)
    # 4.返回响应
    return HttpResponse('ok')


def files(request):
    # 获取 上传的 图片信息
    img = request.FILES.get('img')

    # 获取上传图片的名称
    img_name = img.name

    # 获取后缀
    ext = os.path.splitext(img_name)[1]
    # 重新规定图片名称，图片类型
    img_name = f'avatar-{mobile}{ext}'

    # 图片保存路径
    img_path = os.path.join(settings.IMG_UPLOAD, img_name)

    # 写入 上传图片的 内容
    with open(img_path, 'ab') as fp:
        # 如果上传的图片非常大， 那么通过 img对象的 chunks() 方法 分割成多个片段来上传
        for chunk in img.chunks():
            fp.write(chunk)

    # AxfUser.objects.create_user(
    #     username=username,
    #     password=password,
    #     avatar=f'/static/uploads/{filename}', # 数据库 图片字段 存储路径
    #     mobile=mobile
    # )

    return HttpResponse('uploads success')
