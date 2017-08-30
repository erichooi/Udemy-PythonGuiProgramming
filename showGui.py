# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName("mainDialog")
        mainDialog.resize(361, 82)
        self.nameEdit = QtWidgets.QLineEdit(mainDialog)
        self.nameEdit.setGeometry(QtCore.QRect(20, 30, 221, 24))
        self.nameEdit.setText("")
        self.nameEdit.setObjectName("nameEdit")
        self.showButton = QtWidgets.QPushButton(mainDialog)
        self.showButton.setGeometry(QtCore.QRect(260, 30, 80, 24))
        self.showButton.setObjectName("showButton")

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)
        mainDialog.setTabOrder(self.showButton, self.nameEdit)

    def retranslateUi(self, mainDialog):
        _translate = QtCore.QCoreApplication.translate
        mainDialog.setWindowTitle(_translate("mainDialog", "Main Dialog"))
        self.nameEdit.setPlaceholderText(_translate("mainDialog", "What is your name?"))
        self.showButton.setText(_translate("mainDialog", "Show"))

