#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2021/2/6
# @file 爬取Python100题.py
import re
import requests

def gethtml(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("处理异常")

def extrinfo(txt,i):
    try:
        r=re.findall(r"</strong>.+?</p>",txt)
        r[0]=r[0].replace("</strong>","")
        r[0]=r[0].replace("</p>","")
        print(str(i)+":\t"+r[0])
    except:
        print(str(i)+"\t"+"处理异常")

def main(i):
    url="https://www.runoob.com/python/python-exercise-example"+str(i)+".html"
    extrinfo(gethtml(url),i)

if __name__ == "__main__":
    for i in range(1,101):
        main(i)