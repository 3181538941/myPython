#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/3/16
# @file UDiskAutoBackup.py

import os
import json
import shutil
import logging
import platform
from psutil import disk_partitions


# import openpyxl
# from openpyxl.styles import Alignment

class AutoBackup(object):

    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        self.usb_device = self.get_usb_device()
        self.getMyOnlyDisk()

        self.file_dict = []

    def getData(self):
        with open('data.dat', 'r', encoding='utf-8') as fp:
            li = fp.readlines()
            print([item.strip() for item in li])

    # 获取U盘的盘符
    # disk_partitions() 打印一下他的返回值，就会完全清楚下面这个函数
    def get_usb_device(self):
        devices = []
        for item in disk_partitions():
            if item.opts == "rw,removable":  # 可读、可移动介质
                self.logger.info("发现USB：%s" % str(item))
                devices.append(item.device)
        if devices:
            return devices
        self.logger.info("没有发现USB")

    def getMyOnlyDisk(self):
        for item in self.usb_device:
            print(os.listdir(item))
            if 'leo.ico' in os.listdir(item):
                self.myDisk = item

    def scanDisk(self,disk):
        with open('data.dat', 'w', encoding='utf-8') as fp:

            for dirPath, dirNames, fileNames in os.walk(disk):
                # print(dirPath, dirNames, fileNames)
                # print(os.path.splitdrive(dirPath)[1][1:])
                for file in fileNames:
                    fileAbsPath = os.path.join(dirPath, file)
                    print(fileAbsPath)
                    noDeviceAbsPath = os.path.splitdrive(fileAbsPath)[1][1:]
                    print(noDeviceAbsPath)
                    fp.write(noDeviceAbsPath + '\n')
                    self.file_dict.append(noDeviceAbsPath)

    def writeToFile(self, fileName, content):
        pass


if __name__ == '__main__':
    test = AutoBackup()
    # test.scanDisk(test.myDisk)
    # test.getData()
    print(test.usb_device)
    print(test.myDisk)
