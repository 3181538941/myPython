#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2021/12/30
# @file show.py
import cv2
def showpic():
    img = cv2.imread(r'F:\03_Important\Python\other\12.jpg')
    cv2.imshow('pic', img)
    cv2.waitKey()

if __name__ == '__main__':
    showpic()