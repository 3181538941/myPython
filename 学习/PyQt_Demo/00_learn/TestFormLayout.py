#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2022/7/22
# @file TestFormLayout.py
import sys
from MainWinFormLayout import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


def click_button1(self):
    print('click button')
    print(self.lineEdit_id.text())
    print(self.lineEdit_name.text())
    print(self.spinBox_age.text())
    print(self.combo_privince.currentText())
    print(self.lineEdit_salary.text())


def login(self):
    print('-' * 5 + 'login' + '-' * 5)
    print(self.loginEdit_name.text())
    print(self.loginEdit_passwd.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    # 为下拉框设置数据
    ui.combo_privince.addItems(['北京', '吉林', '海南', '上海', '广东'])

    # 将点击信号绑定到按钮
    ui.pushButton1.clicked.connect(lambda: click_button1(ui))
    ui.pushButton2.clicked.connect(lambda: login(ui))
    mainWindow.show()
    sys.exit(app.exec_())
