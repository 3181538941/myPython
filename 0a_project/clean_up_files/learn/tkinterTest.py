#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/1/8
# @file tkinterTest.py
import os
from pprint import pprint


class ViewFile(object):
    def __init__(self, path, kwargs):
        self.allFile = {}
        self.path = path
        self.hasMoved = []
        self.clean(path, kwargs)

    def viewTarget(self, dirPath):
        pass
        # todo view the goal dir and list files to judge
        fileList = os.listdir(dirPath)
        return fileList

    def clean(self, path, kwargs):
        fileList = os.listdir(path)
        for item in fileList:
            absPath = os.path.join(path, item)
            # todo walk
            if os.path.isdir(absPath):
                # todo append dirName
                self.clean(absPath, kwargs)
            else:
                for typ in kwargs.keys():
                    if item.endswith(typ):
                        if typ not in self.allFile.keys():
                            self.allFile[typ] = []
                        self.allFile[typ].append(item)
                        if item not in self.viewTarget(kwargs[typ]):
                            os.popen(rf'move {absPath} {kwargs[typ]}')
                            self.hasMoved.append(item)


# path = r'F:\03_Important\Python\0a_project\clear_up_files'
path = r'E:\Download'

dic = {'exe': r'E:\Download\exes',
       'zip': r'E:\Download\Compressed',
       'rar': r'E:\Download\Compressed'}

# list = ViewFile(path, dic)
# # pprint(list.allFile)
# pprint(list.hasMoved)

import tkinter as tk
from PIL import Image, ImageTk

x = 0


class GUI:
    def click(self, step):
        global x
        x += step
        print(x)

    def st1(self):
        self.click(1)

    def st2(self):
        self.click(2)

    def show(self):
        # 初始化Tk
        myWindow = tk.Tk()
        # 加载tk主题
        myWindow.tk.call("source", r"F:\03_Important\Python\0a_project\Azure-ttk-theme-main\azure.tcl")
        myWindow.tk.call("set_theme", 'light')
        # 设置标题
        myWindow.title('fileCleaner')
        # 设置窗口大小
        width = 600
        height = 300
        # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
        screenWidth = myWindow.winfo_screenwidth()
        screenHeight = myWindow.winfo_screenheight()
        locateWidth = int((screenWidth - width) / 2)
        locateHeight = int((screenHeight - height) / 2)
        myWindow.geometry(f'{width}x{height}+{locateWidth}+{locateHeight}')
        # 设置窗口是否可变长、宽
        myWindow.resizable(width='False', height='True')
        # 设置窗口图标
        myWindow.iconbitmap('terminal.ico')
        # 创建一个标签用来显示文本
        tk.Label(myWindow, text='username', bg='red').place(x=10, y=70, height=30, width=120)
        tk.Label(myWindow, text='password', bg='green').place(x=10, y=100, height=30, width=120)
        # 使用PIL的Image打开图片
        # img = Image.open(r'F:\03_Important\Python\0a_project\clear_up_files\learn\beihua.jpg')
        img = Image.open(r'beihua.png')
        # 设定图片大小
        img = img.resize((50, 50))
        # 将PIL的Image对象转化为Tk的Image对象
        image = ImageTk.PhotoImage(img)
        # 将图片对象插入到标签中
        tk.Label(myWindow, image=image, height=40, width=50, bg='#dadada').place(relx=0.01, rely=0.01)
        # 添加文本标签
        explanation = """At present, only GIF and PPM/PGM
        formats are supported, but an interface
        exists to allow additional image file
        formats to be added easily."""
        tk.Label(myWindow, text=explanation, bg='#dadada').place(x=200, y=100, height=100, width=400)
        # 插入按钮对象
        from tkinter import ttk

        # 创建框架, 用来存放按钮
        # fra = tk.Frame(myWindow, bg='#e0e0df')
        fra = tk.Frame(myWindow)
        ttk.Button(fra, text='按一下1', command=self.st1, style="Accent.TButton").place(relwidth=0.45, relheight=1)
        ttk.Button(fra, text='按一下2', command=self.st2, style="Toggle.TButton").place(relx=0.5, relwidth=0.45, relheight=1)
        fra.place(x=10, y=250, height=40, width=200)

        fra_entry = tk.Frame(myWindow)
        lab1 = tk.Label(fra_entry, text='user').place(relheight=0.5, relwidth=.3)
        lab2 = tk.Label(fra_entry, text='passwd').place(relheight=0.5, rely=0.5, relwidth=.3)
        self.entry1 = tk.Entry(lab1)
        self.entry1.place(height=30, width=185, x=302, y=15)
        self.entry2 = tk.Entry(lab2)
        self.entry2.place(height=30, width=185, x=302, y=60)
        fra_entry.place(x=200, height=100, width=300)

        fra2 = tk.Frame(myWindow)
        ttk.Button(fra2, text='获取user', command=self.getEntry1, style="Accent.TButton").place(y=5,relwidth=1,height=40)
        ttk.Button(fra2, text='插入', command=self.insertEntry2, style="Toggle.TButton").place(y=55, relwidth=1, height=40)
        fra2.place(x=500, height=100, width=100)
        # 进入消息循环
        myWindow.mainloop()

    def getEntry1(self):
        value = self.entry1.get()
        print(value)
        return value

    def getEntry2(self):
        value = self.entry2.get()
        print(value)

    def insertEntry2(self):
        self.entry2.delete(0, len(self.entry2.get()))
        self.entry2.insert(0, self.getEntry1())
        # self.entry2.delete(0, len(self.entry2.get()))
        # self.entry2.insert(2, '12345')


if __name__ == '__main__':
    gui = GUI()
    gui.show()
