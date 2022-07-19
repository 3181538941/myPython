#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/7/19
# @file 01_simple.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QPlainTextEdit, QMessageBox


class AppDemo:
    def __init__(self):
        # 初始化应用程序
        self.app = QApplication([])
        # 初始化窗口控件
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 310)
        self.window.setWindowTitle('薪资统计')
        # 初始化纯文本控件
        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("请输入薪资表")
        self.textEdit.move(10, 10)
        self.textEdit.resize(350, 380)
        # 初始化按钮
        self.button = QPushButton('统计', self.window)
        self.button.move(380, 80)
        self.button.resize(50, 30)

        # 将点击信号绑定到按钮
        self.button.clicked.connect(self.handle_click)

    def handle_click(self):
        info = self.textEdit.toPlainText()

        # 薪资20000 以上 和 以下 的人员名单
        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')
            # 去掉列表中的空字符串内容
            parts = [p for p in parts if p]
            name, salary, age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(
            self.window,
            '统计结果',
            f'薪资20000 以上的有：\n{salary_above_20k}\n\n'
            f'薪资20000 以下的有：\n{salary_below_20k}'
        )

    def run(self):
        self.window.show()
        self.app.exec_()


if __name__ == '__main__':
    demo = AppDemo()
    demo.run()
