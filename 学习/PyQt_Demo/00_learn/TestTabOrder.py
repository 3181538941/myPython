#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/7/25
# @file TestTabOrder.py
import sys
from MainWinTabOrder import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    # 添加控件
    
    mainWindow.show()
    sys.exit(app.exec_())