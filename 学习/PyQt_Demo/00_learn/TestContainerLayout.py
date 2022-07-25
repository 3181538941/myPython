#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/7/22
# @file TestFormLayout.py
import sys
from MainWinContainerLayout import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    ui.pushButton.setText('按钮')
    print(ui.pushButton.sizeHint())
    mainWindow.show()
    sys.exit(app.exec_())
