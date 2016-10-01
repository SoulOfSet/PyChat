from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow


class WindowAuth(QtWidgets.QDialog):

    #Window manager
    _windowManager = ""


    def __init__(self, manager):
        super().__init__()
        self._windowManager = manager
        self.setupUI(self)
        
      
        
    def setupUI(self, WindowAuth):
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
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.retranslateUi(WindowAuth)
        QtCore.QMetaObject.connectSlotsByName(WindowAuth)

    def retranslateUi(self, WindowAuth):
        _translate = QtCore.QCoreApplication.translate
        WindowAuth.setWindowTitle(_translate("WindowAuth", "Dialog"))
        self.usernameLabel.setText(_translate("WindowAuth", "Username"))
        self.authTitleLabel.setText(_translate("WindowAuth", "Authenticate"))
        self.pushButton.setText(_translate("WindowAuth", "Submit"))

    def quit(self):
        sys.exit()