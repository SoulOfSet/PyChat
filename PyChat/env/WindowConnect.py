from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow


class WindowConnect(QtWidgets.QDialog):

    #Window manager
    _windowManager = ""


    def __init__(self, manager):
        super().__init__()
        self._windowManager = manager
        self.setupUI(self)
        
      
        
    def setupUI(self, ConnectWindow):               
        
        ConnectWindow.setObjectName("ConnectWindow")
        ConnectWindow.resize(400, 300)

        self.titleLabel = QtWidgets.QLabel(ConnectWindow)
        self.titleLabel.setGeometry(QtCore.QRect(40, 20, 331, 41))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(24)

        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")

        self.addressLabel = QtWidgets.QLabel(ConnectWindow)
        self.addressLabel.setGeometry(QtCore.QRect(50, 87, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addressLabel.setFont(font)
        self.addressLabel.setObjectName("addressLabel")

        self.portLabel = QtWidgets.QLabel(ConnectWindow)
        self.portLabel.setGeometry(QtCore.QRect(50, 167, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.portLabel.setFont(font)
        self.portLabel.setObjectName("portLabel")

        self.addressInput = QtWidgets.QLineEdit(ConnectWindow)
        self.addressInput.setGeometry(QtCore.QRect(150, 110, 211, 20))
        self.addressInput.setObjectName("addressInput")

        self.portInput = QtWidgets.QLineEdit(ConnectWindow)
        self.portInput.setGeometry(QtCore.QRect(150, 190, 211, 20))
        self.portInput.setObjectName("portInput")

        self.errorLabel = QtWidgets.QLabel(ConnectWindow)
        self.errorLabel.setGeometry(QtCore.QRect(120, 200, 200, 61))
        self.errorLabel.setObjectName("errorLabel")

        self.connectBtn = QtWidgets.QPushButton(ConnectWindow)
        self.connectBtn.setGeometry(QtCore.QRect(150, 240, 100, 51))
        self.connectBtn.setObjectName("connectBtn")
        self.connectBtn.clicked.connect(lambda: self.connectBtnClick(self.addressInput.text(), self.portInput.text()))

        self.retranslateUi(ConnectWindow)
        QtCore.QMetaObject.connectSlotsByName(ConnectWindow)

    def retranslateUi(self, ConnectWindow):
        _translate = QtCore.QCoreApplication.translate
        ConnectWindow.setWindowTitle(_translate("ConnectWindow", "Connect"))
        self.titleLabel.setText(_translate("ConnectWindow", "Enter server information"))
        self.addressLabel.setText(_translate("ConnectWindow", "Address"))
        self.portLabel.setText(_translate("ConnectWindow", "Port"))
        self.connectBtn.setText(_translate("ConnectWindow", "Connect"))

        
    def quit(self):
        sys.exit()

    def connectBtnClick(self, address, port):
        if(address == "" or port == "" or port.isdigit() == False):
            self.errorLabel.setText("Please input a valid port and/or address")
        else:
            if(self._windowManager.guiEventHandler("CLIENT_ATTEMPT_CONNECT", port=port, address=address)):
                self.destroy()
            else:
                self.errorLabel.setText("Unable to connect")
                