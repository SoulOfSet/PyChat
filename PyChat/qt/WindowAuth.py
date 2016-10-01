# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowauth.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WindowAuth(object):
    def setupUi(self, WindowAuth):
        WindowAuth.setObjectName("WindowAuth")
        WindowAuth.resize(400, 300)
        self.usernameLabel = QtWidgets.QLabel(WindowAuth)
        self.usernameLabel.setGeometry(QtCore.QRect(30, 100, 100, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.lineEdit = QtWidgets.QLineEdit(WindowAuth)
        self.lineEdit.setGeometry(QtCore.QRect(140, 112, 200, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.authTitleLabel = QtWidgets.QLabel(WindowAuth)
        self.authTitleLabel.setGeometry(QtCore.QRect(110, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(24)
        self.authTitleLabel.setFont(font)
        self.authTitleLabel.setObjectName("authTitleLabel")
        self.pushButton = QtWidgets.QPushButton(WindowAuth)
        self.pushButton.setGeometry(QtCore.QRect(150, 220, 100, 50))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(WindowAuth)
        QtCore.QMetaObject.connectSlotsByName(WindowAuth)

    def retranslateUi(self, WindowAuth):
        _translate = QtCore.QCoreApplication.translate
        WindowAuth.setWindowTitle(_translate("WindowAuth", "Dialog"))
        self.usernameLabel.setText(_translate("WindowAuth", "Username"))
        self.authTitleLabel.setText(_translate("WindowAuth", "Authenticate"))
        self.pushButton.setText(_translate("WindowAuth", "Submit"))

