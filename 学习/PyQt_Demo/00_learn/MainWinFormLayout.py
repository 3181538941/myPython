# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWinFormLayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 269)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(250, 90, 201, 82))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.loginEdit_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.loginEdit_name.setObjectName("loginEdit_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.loginEdit_name)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.loginEdit_passwd = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.loginEdit_passwd.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.loginEdit_passwd.setText("")
        self.loginEdit_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginEdit_passwd.setObjectName("loginEdit_passwd")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.loginEdit_passwd)
        self.pushButton2 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton2.setObjectName("pushButton2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton2)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 211, 202))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_id = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_id.sizePolicy().hasHeightForWidth())
        self.label_id.setSizePolicy(sizePolicy)
        self.label_id.setObjectName("label_id")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_id)
        self.lineEdit_id = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_id)
        self.label_name = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_name)
        self.label_age = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_age.sizePolicy().hasHeightForWidth())
        self.label_age.setSizePolicy(sizePolicy)
        self.label_age.setObjectName("label_age")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_age)
        self.spinBox_age = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_age.setObjectName("spinBox_age")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.spinBox_age)
        self.label_province = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_province.sizePolicy().hasHeightForWidth())
        self.label_province.setSizePolicy(sizePolicy)
        self.label_province.setObjectName("label_province")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_province)
        self.label_salary = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_salary.sizePolicy().hasHeightForWidth())
        self.label_salary.setSizePolicy(sizePolicy)
        self.label_salary.setObjectName("label_salary")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_salary)
        self.lineEdit_salary = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_salary.setObjectName("lineEdit_salary")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_salary)
        self.lineEdit_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name)
        self.pushButton1 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton1.setObjectName("pushButton1")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.pushButton1)
        self.combo_privince = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_privince.setObjectName("combo_privince")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.combo_privince)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "name"))
        self.label_7.setText(_translate("MainWindow", "passwd"))
        self.pushButton2.setText(_translate("MainWindow", "Button2"))
        self.label_id.setText(_translate("MainWindow", "??????: "))
        self.label_name.setText(_translate("MainWindow", "??????: "))
        self.label_age.setText(_translate("MainWindow", "??????: "))
        self.label_province.setText(_translate("MainWindow", "??????: "))
        self.label_salary.setText(_translate("MainWindow", "??????: "))
        self.pushButton1.setText(_translate("MainWindow", "Button1"))
