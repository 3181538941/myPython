#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/6/4
# @file 计算保质期.py
import datetime

produce_date = datetime.datetime.strptime(input('请输入生产日期: (例如20220604): '), '%Y%m%d')
today = datetime.datetime.now()  # 当前日期
shelfLife = int(input('请输入保质期(天): '))  # 保质期
delta = datetime.timedelta(days=shelfLife)  # 保质期时间间隔
expire_date = (produce_date + delta)  # 有效期至
delta = expire_date - today  # 剩余天数
print('当前日期: ', today.strftime("%Y-%m-%d"))
print('有效期至: ', expire_date.strftime("%Y-%m-%d"))
print('剩余天数: ', delta.days)
