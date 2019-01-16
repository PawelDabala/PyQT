# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'master_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(487, 460)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(50, 40, 411, 201))
        self.tableView.setObjectName("tableView")
        self.lineEdit_add = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_add.setGeometry(QtCore.QRect(60, 261, 181, 20))
        self.lineEdit_add.setObjectName("lineEdit_add")
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        self.pushButton_add.setGeometry(QtCore.QRect(250, 260, 75, 23))
        self.pushButton_add.setObjectName("pushButton_add")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_add.setText(_translate("Dialog", "Dodaj"))

