#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/1/15
# @file GUI_achieve.py

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
from util import *


class GUI(object):
    def __init__(self):
        self.workDir = None
        self.showGUI()

    def showGUI(self):
        # 初始化Tk
        self.root = Tk()
        # 设置标题
        self.root.title('fileCleaner')
        # 加载tk主题
        self.root.call("source", r"F:\03_Important\Python\0a_project\Azure-ttk-theme-main\azure.tcl")
        self.root.call("set_theme", 'light')
        # 设置窗口大小
        width = 800
        height = 600
        # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        locateWidth = int((screenWidth - width) / 2)
        locateHeight = int((screenHeight - height) / 2)
        self.root.geometry(f'{width}x{height}+{locateWidth}+{locateHeight}')
        # 设置窗口是否可变长、宽
        self.root.resizable(width='False', height='True')
        # 设置窗口图标
        self.root.iconbitmap('../learn/terminal.ico')
        self.button_choose = Button(self.root,
                                    text='选择目录',
                                    command=self.chooseDir,
                                    bd=0,
                                    bg='#3398ff',
                                    font=('黑体', 12)
                                    )
        self.button_choose.place(x=650, y=20, width=120, height=40)
        self.button_test = Button(self.root,
                                  text='判断',
                                  command=self.judgePathEntry,
                                  bd=0,
                                  bg='#3398ff',
                                  font=('黑体', 12)
                                  )
        self.button_test.place(x=650, y=80, width=120, height=40)
        # self.dirPathVar = StringVar()
        # self.showDirPath = Label(self.root, textvariable=self.dirPathVar, bg='#dadada')
        Label(self.root,
              text="文件夹路径:",
              font=('黑体', 12)
              ).place(x=10, y=20, height=40, width=120)
        self.showDirPathEntry = Entry(self.root,
                                      bg='#dadada',
                                      bd=1,
                                      font=('小米兰亭Pro', 14),
                                      justify='center')
        self.showDirPathEntry.place(x=150, y=20, height=40, width=470)

        # todo 根据日志文本长度动态改变文本标签的高度, 适当加一下可拖动的进度条

        self.root.mainloop()

    def judgePathEntry(self):
        path = self.showDirPathEntry.get()
        print('111' if isDir(path) else '000')

    def chooseDir(self):
        self.workDir = askdirectory()
        # self.showDirPathEntry.set(self.workDir)
        self.showDirPathEntry.delete(0, len(self.showDirPathEntry.get()))
        self.showDirPathEntry.insert(0, self.workDir)


if __name__ == '__main__':
    gui = GUI()
# gui.chooseDir()
