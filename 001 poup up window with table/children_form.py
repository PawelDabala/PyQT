# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'children_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 47, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(210, 20, 131, 16))
        self.label_3.setObjectName("label_3")
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(220, 260, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 230, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(320, 80, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(20, 40, 231, 171))
        self.listView.setObjectName("listView")
        self.pushButton_remove = QtWidgets.QPushButton(Form)
        self.pushButton_remove.setGeometry(QtCore.QRect(20, 260, 75, 23))
        self.pushButton_remove.setObjectName("pushButton_remove")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "rok"))
        self.label_2.setText(_translate("Form", "klient"))
        self.label_3.setText(_translate("Form", "sale house"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.radioButton.setText(_translate("Form", "RadioButton"))
        self.pushButton_remove.setText(_translate("Form", "remove"))

