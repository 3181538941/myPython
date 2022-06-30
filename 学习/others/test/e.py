#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/3/29
# @file Email.py
import yagmail

# 链接邮箱服务器user@126.com发件人邮箱
# 1234发件人邮箱侵权码（授权码·注意不是邮辐密码）
# smtp.126.com网易126邮箱发件服务器
yag = yagmail.SMTP(user="leolswq@163.com", password="AVPBLRPCZTUXCYUS", host='smtp.163.com')
# 邮箱正文contents 【'This is the body,and here is just text http://somedomain/image.png'，
contents = ['You can find an audio file attached.']
# 发送邮件
# taaa@126.com收件人邮箱subject邮件生题
yag.send('3181538941@qq.com', 'subject', contents)
