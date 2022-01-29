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
        self.dicAll = {
            '压缩文件'   : '7z gz rar zip',
            '可执行文件'  : 'exe',
            '图片'     : 'png jpg jpeg',
            '文档'     : 'txt doc docx pdf epub',
            '演示文档及表格': 'ppt pptx xls xlsx csv',
            '图标'     : 'ico',
            '视频'     : 'mp4 mkv avi',
            'GIF'    : 'gif',
            '音乐'     : 'mp3',
            '空'      : ''
        }
        self.showGUI()
        # self.showInfoGUI()

    def showGUI(self):
        # 初始化Tk
        self.root = Tk()
        # 设置标题
        self.root.title('fileTool')
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
        self.root.iconbitmap(r'F:\03_Important\Python\0a_project\clean_up_files\com\lswq.ico')
        self.button_choose = Button(self.root,
                                    text='选择目录',
                                    command=lambda: self.chooseDir(self.showDirPathEntry),
                                    bd=0,
                                    bg='#00A4FF',
                                    font=('黑体', 12)
                                    )
        self.button_choose.place(x=650, y=20, width=120, height=40)

        # self.dirPathVar = StringVar()
        # self.showDirPath = Label(self.root, textvariable=self.dirPathVar, bg='#dadada')
        Label(self.root,
              text="文件夹路径:",
              font=('黑体', 12)
              ).place(x=10, y=20, height=40, width=120)
        self.showDirPathEntry = ttk.Entry(self.root,
                                          # bg='#dadada',
                                          # bd=1,
                                          font=('小米兰亭Pro', 14),
                                          justify='center')
        self.showDirPathEntry.place(x=150, y=20, height=40, width=470)

        Label(self.root,
              text="文件操作:",
              font=('黑体', 12),
              ).place(height=60, width=120, x=200, y=110, )

        self.dealMode = IntVar()  # 创建变量, 用来存储复选框被选中状态
        self.dealMode.set(1)  # 设置默认值
        # 文件操作复选框
        Radiobutton(self.root,
                    text='移动',
                    variable=self.dealMode,
                    value=1,
                    font=('黑体', 10),
                    bg='#00A4FF',
                    indicatoron=False).place(width=60, height=30, x=330, y=126)
        Radiobutton(self.root,
                    text='复制',
                    variable=self.dealMode,
                    value=2,
                    font=('黑体', 10),
                    bg='#00A4FF',
                    indicatoron=False).place(width=60, height=30, x=400, y=126)

        Label(self.root,
              text="文件类型:",
              font=('黑体', 12),
              ).place(x=40, y=200, height=40, width=120)
        Label(self.root,
              text="目标路径:",
              font=('黑体', 12),
              ).place(x=240, y=200, height=40, width=120)

        chosen = self.dicAll.keys()
        chosen = tuple(chosen)
        end_chosen = len(chosen) - 1
        self.typ1 = StringVar()
        self.typ2 = StringVar()
        self.typ3 = StringVar()
        self.typ4 = StringVar()

        self.pth1 = StringVar()
        self.pth2 = StringVar()
        self.pth3 = StringVar()
        self.pth4 = StringVar()

        tpyChosen1 = ttk.Combobox(self.root, textvariable=self.typ1, value=chosen, font=('黑体', 10))
        tpyChosen2 = ttk.Combobox(self.root, textvariable=self.typ2, value=chosen, font=('黑体', 10))
        tpyChosen3 = ttk.Combobox(self.root, textvariable=self.typ3, value=chosen, font=('黑体', 10))
        tpyChosen4 = ttk.Combobox(self.root, textvariable=self.typ4, value=chosen, font=('黑体', 10))

        pthChosen1 = ttk.Entry(self.root, textvariable=self.pth1, font=('黑体', 10))
        pthChosen2 = ttk.Entry(self.root, textvariable=self.pth2, font=('黑体', 10))
        pthChosen3 = ttk.Entry(self.root, textvariable=self.pth3, font=('黑体', 10))
        pthChosen4 = ttk.Entry(self.root, textvariable=self.pth4, font=('黑体', 10))

        # 设置下拉列表默认显示的值
        tpyChosen1.current(end_chosen)
        tpyChosen2.current(end_chosen)
        tpyChosen3.current(end_chosen)
        tpyChosen4.current(end_chosen)

        # 设置左面4个位置
        configTpy = {'width': 160, 'height': 35, 'x': 50, }
        tpyChosen1.place(**configTpy, y=250)
        tpyChosen2.place(**configTpy, y=300)
        tpyChosen3.place(**configTpy, y=350)
        tpyChosen4.place(**configTpy, y=400)

        configPth = {'width': 320, 'height': 35, 'x': 245, }
        pthChosen1.place(**configPth, y=250)
        pthChosen2.place(**configPth, y=300)
        pthChosen3.place(**configPth, y=350)
        pthChosen4.place(**configPth, y=400)

        self.pthChoseButton1 = Button(self.root, text='选择目录', command=lambda: self.chooseDir(pthChosen1), bd=0, bg='#00A9FF',
                                      font=('黑体', 10))
        self.pthChoseButton2 = Button(self.root, text='选择目录', command=lambda: self.chooseDir(pthChosen2), bd=0, bg='#00A9FF',
                                      font=('黑体', 10))
        self.pthChoseButton3 = Button(self.root, text='选择目录', command=lambda: self.chooseDir(pthChosen3), bd=0, bg='#00A9FF',
                                      font=('黑体', 10))
        self.pthChoseButton4 = Button(self.root, text='选择目录', command=lambda: self.chooseDir(pthChosen4), bd=0, bg='#00A9FF',
                                      font=('黑体', 10))

        configPthButton = {'width': 100, 'height': 35, 'x': 600, }
        self.pthChoseButton1.place(**configPthButton, y=250)
        self.pthChoseButton2.place(**configPthButton, y=300)
        self.pthChoseButton3.place(**configPthButton, y=350)
        self.pthChoseButton4.place(**configPthButton, y=400)

        self.button_test = Button(self.root,
                                  text='执行',
                                  command=self.mainProcess,
                                  bd=0,
                                  bg='#F5D413',
                                  font=('黑体', 14)
                                  )
        self.button_test.place(x=(width - 120) / 2, y=500, width=120, height=40)

        # 进入主循环
        self.root.mainloop()

    def showInfoGUI(self, info, warn=0):
        # 初始化Tk
        self.mes = Toplevel()

        # 设置标题
        self.mes.title('fileTool')
        if warn == 0:
            # 设置窗口大小
            width = 700
            height = 500
        else:
            width = 200
            height = 80
        # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
        screenWidth = self.mes.winfo_screenwidth()
        screenHeight = self.mes.winfo_screenheight()
        locateWidth = int((screenWidth - width) / 2)
        locateHeight = int((screenHeight - height) / 2)
        self.mes.geometry(f'{width}x{height}+{locateWidth}+{locateHeight}')
        # 设置窗口是否可变长、宽
        self.mes.resizable(width='True', height='True')
        # 设置窗口图标
        self.mes.iconbitmap(r'F:\03_Important\Python\0a_project\clean_up_files\com\lswq.ico')

        # print(self.messageString.get())

        # 设置窗口透明度
        self.mes.attributes('-alpha', 0.9)
        # 文本控件
        text = Text(self.mes, width=width, font=('小米兰亭Pro', 12), )
        if warn == 1:
            text.config(bg='#F92672', fg='#FFFFFF')
        # 创建滚动条
        scroll = Scrollbar(self.mes)
        # side:将滚动条放到主窗体右侧  fill:将窗体Y侧填充满
        scroll.pack(side=RIGHT, fill=Y)
        # 将字符串内容添加到文本中
        text.insert(INSERT, info)
        # side:将文本放到主窗体左侧 fill:将窗体Y侧填充满
        text.pack(side=LEFT, fill=Y)

        scroll.config(command=text.yview)
        text.config(yscrollcommand=scroll.set)

        # self.textShadow = Message(self.mes,
        #                           textvariable=self.messageString,
        #                           bg='#dadada',
        #                           font=('小米兰亭Pro', 12),
        #                           width=width,
        #
        #                           )
        # self.textShadow.place(x=0, y=0, width=width)

        self.mes.mainloop()

    def judgePathEntry(self):
        self.path = self.showDirPathEntry.get()
        return True if isDir(self.path) else False

    def chooseExceptFile(self):
        self.exceptList = []

    def chooseDir(self, var):
        self.workDir = askdirectory()
        # self.showDirPathEntry.delete(0, len(self.showDirPathEntry.get()))
        var.delete(0, END)
        var.insert(0, self.workDir)

    def mainProcess(self):

        if not self.judgePathEntry():
            self.showInfoGUI('path ERROR', 1)
            return 'Error'
        dicChoose = {
            self.dicAll[self.typ1.get()]: self.pth1.get(),
            self.dicAll[self.typ2.get()]: self.pth2.get(),
            self.dicAll[self.typ3.get()]: self.pth3.get(),
            self.dicAll[self.typ4.get()]: self.pth4.get()
        }
        exceptList = ['云盘缓存.zip']
        dealDic = {
            1: 'move', 2: 'copy'
        }
        test = ViewFile(dicChoose)
        # 调用主要方法
        test.clean(self.showDirPathEntry.get(), dealDic[self.dealMode.get()], exceptList=exceptList)
        st = ''
        dicReset = {
            '7z gz rar zip'        : '压缩文件',
            'exe'                  : '可执行文件',
            'png jpg jpeg'         : '图片',
            'txt doc docx pdf epub': '文档',
            'ppt pptx xls xlsx csv': '演示文档及表格',
            'ico'                  : '图标',
            'mp4 mkv avi'          : '视频',
            'gif'                  : 'GIF',
            'mp3'                  : '音乐',
            ''                     : '空'
        }
        # for i in dealDic.keys():
        #     st += (f'{fileTypeNameDic[i]}有 {len(test.allFile[i])} 个, 分别为:\n {test.allFile[i]}\n')
        # self.messageString.set(st + st + f'移动了 {len(test.toMoveFile)} 个文件, 分别为:\n {test.toMoveFile}\n')
        # print((st+f'移动了 {len(test.toMoveFile)} 个文件, 分别为:\n {test.toMoveFile}'))
        # info = f'{dicChoose} \n' \
        #        f' {test.toMoveFile}' + f'移动了 {len(test.toMoveFile)} 个文件, 分别为:\n {test.toMoveFile}\n'
        info = f'\n\t\t\t处理了 {len(test.hasDeal)} 个文件: \n\n'
        for fileType in dicChoose.keys():
            if fileType != '':
                info += f'{dicReset[fileType]} 有 {len(test.allFile[fileType])} 个, 分别为:\n\t'
                files = '\n\t'.join(test.allFile[fileType])
                info += f"{files}\n\n"
            # f'{list(dicChoose.keys())[1]} 文件有 {len(test.allFile[list(dicChoose.keys())[1]])} 个'
            # f'{list(dicChoose.keys())[2]} 文件有 {len(test.allFile[list(dicChoose.keys())[2]])} 个'
            # f'{list(dicChoose.keys())[3]} 文件有 {len(test.allFile[list(dicChoose.keys())[3]])} 个'
        self.showInfoGUI(info)

        # outputLogToExcel(r'.\log.xlsx', test.toMove)
        import datetime
        if test.toMove:
            with open('.\log.txt','a',encoding='utf-8') as log:
                t = f'\n\n{datetime.datetime.now()}\n'
                for item in test.toMove:
                    t += "\t".join(item)
                    t += '\n'

                log.write(t)
        # print(test.toMove)


if __name__ == '__main__':
    gui = GUI()
# gui.chooseDir()
