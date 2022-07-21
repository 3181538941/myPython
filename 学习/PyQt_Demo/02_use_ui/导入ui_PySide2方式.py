#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/7/20
# @file 导入ui_PySide2方式.py
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QPlainTextEdit, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import sys


class MainWindow:
    def __init__(self):
        # 必须在父类初始化之前调用, 否则返回代码 -1073740791 (0xC0000409)
        self.app = QApplication(sys.argv)
        # 从文件中加载ui定义
        self.file = QFile('simple.ui')
        self.file.open(QFile.ReadOnly)
        self.file.close()
        # 从ui定义中动态生成窗口对象
        self.ui = self.QUiLoader().load(self.file)

        # 将点击信号绑定到按钮
        self.ui.pushButton.clicked.connect(self.handle_click)

    def handle_click(self):
        info = self.ui.toPlainText()

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
            self.ui.centralwidget,
            '统计结果',
            f'薪资20000 以上的有：\n{salary_above_20k}\n\n'
            f'薪资20000 以下的有：\n{salary_below_20k}'
        )


if __name__ == '__main__':
    demo = MainWindow()
    demo.show()
    sys.exit(demo.app.exec_())
