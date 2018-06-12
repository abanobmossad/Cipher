# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'key_generation.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(243, 113)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color:\"#2c3e50\";\n"
                             "color:\"#71BA51\"")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 50, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setValue(0)
        self.spinBox.setGeometry(QtCore.QRect(161, 50, 61, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(41, 50, 61, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setValue(0)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 5, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.OK = QtWidgets.QPushButton(Dialog)
        self.OK.setGeometry(QtCore.QRect(150, 80, 75, 23))
        self.OK.setStyleSheet("background-color:\"#71BA51\";\n"
                                      "color:\"#fff\"")
        self.OK.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Generate keys"))
        self.label.setText(_translate("Dialog", "P:"))
        self.label_2.setText(_translate("Dialog", "Q: "))
        self.label_3.setText(_translate("Dialog", "Enter your p and q to generate the keys"))
        self.OK.setText(_translate("Dialog", "OK"))
