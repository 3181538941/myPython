#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/1/8
# @file tkinterTest.py
import os
from pprint import pprint


class ViewFile(object):
    def __init__(self, path, **kwargs):
        self.allFile = {}
        self.path = path
        self.viewFile(path, **kwargs)

    def viewFile(self, path, **kwargs):
        fileList = os.listdir(path)
        for item in fileList:
            absPath = os.path.join(path, item)
            if os.path.isdir(absPath):
                # todo append dirName
                self.viewFile(absPath, **kwargs)
                pass
            else:
                # file = os.path.split(absPath)[1]
                # todo move
                for typ in kwargs.keys():
                    if item.endswith(typ):
                        if typ not in self.allFile.keys():
                            self.allFile[typ] = []
                        self.allFile[typ].append(item)

                        # os.popen(rf'move {absPath} {kwargs[typ]}')


# path = r'F:\03_Important\Python\0a_project\clear_up_files'
path = r'E:\Download'

dic = {'exe': r'E:\Download\exes',
       'zip': '',
       'rar': ''}

# list = ViewFile(path,**dic)
# pprint(list.allFile)


import tkinter as tk
from PIL import Image,ImageTk
x=0
def click():
    global x
    x+=1
    print(x)

# 初始化Tk
myWindow = tk.Tk()
# 设置标题
myWindow.title('fileCleaner')
# 设置窗口大小
width  = 600
height = 300
# 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenWidth  = myWindow.winfo_screenwidth()
screenHeight = myWindow.winfo_screenheight()
locateWidth  = int((screenWidth  - width ) / 2)
locateHeight = int((screenHeight - height) / 2)
myWindow.geometry(f'{width}x{height}+{locateWidth}+{locateHeight}')
# 设置窗口是否可变长、宽
myWindow.resizable(width='False', height='True')
# 设置窗口图标
myWindow.iconbitmap('terminal.ico')
# 创建一个标签用来显示文本
tk.Label(myWindow, text='username',bg='red').place(x=10,y=70,height=30,width=120)
tk.Label(myWindow, text='password',bg='green').place(x=10,y=100,height=30,width=120)
# 使用PIL的Image打开图片
# img = Image.open(r'F:\03_Important\Python\0a_project\clear_up_files\learn\beihua.jpg')
img = Image.open(r'beihua.png')
# 设定图片大小
img = img.resize((50,50))
# 将PIL的Image对象转化为Tk的Image对象
image = ImageTk.PhotoImage(img)
# 将图片对象插入到标签中
tk.Label(myWindow, image=image,height=40,width=50,bg='#dadada').place(relx=0.01,rely=0.01)
# 添加文本标签
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface
exists to allow additional image file
formats to be added easily."""
tk.Label(myWindow,text=explanation,bg='#dadada').place(x=200,y=100,height=100,width=400)
tk.Button(myWindow,text='按一下',command=click).place(x=100,y=30)
# 进入消息循环
myWindow.mainloop()

