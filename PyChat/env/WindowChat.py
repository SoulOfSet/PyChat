from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow
from env import WindowConnect, WindowAuth


class WindowChat(QMainWindow):

    #Window manager
    _windowManager = ""


    #Prefix
    _prefixNext = False
    _prefix = ""

    def __init__(self, manager):
        super().__init__()
        self._windowManager = manager
        self.setupUI(self)
        
      
        
    def setupUI(self, ChatWindow):               
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        ChatWindow.setObjectName("ChatWindow")
        ChatWindow.resize(803, 613)
        ChatWindow.setFixedSize(803, 613)

        self.centralwidget = QtWidgets.QWidget(ChatWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Vertical layout for the connected user list
        self.userListWidget = QtWidgets.QWidget(self.centralwidget)
        self.userListWidget.setGeometry(QtCore.QRect(600, 0, 599, 490))
        self.userListWidget.setObjectName("userListWidget")
        self.userListLayout = QtWidgets.QVBoxLayout(self.userListWidget)
        self.userListLayout.setContentsMargins(0, 0, 0, 0)
        self.userListLayout.setObjectName("userListLayout")
        self.userList = QtWidgets.QListView(self.userListWidget)
        self.userList.setObjectName("userList")
        self.userListLayout.addWidget(self.userList)
        self.userModel = QtGui.QStandardItemModel(self.userList)
        self.userList.setModel(self.userModel)

        #Vertical layout for the chat input
        self.chatInputWidget = QtWidgets.QWidget(self.centralwidget)
        self.chatInputWidget.setGeometry(QtCore.QRect(0, 499, 701, 73))
        self.chatInputWidget.setObjectName("chatInputWidget")
        self.chatInLayout = QtWidgets.QVBoxLayout(self.chatInputWidget)
        self.chatInLayout.setContentsMargins(0, 0, 0, 0)
        self.chatInLayout.setObjectName("chatInLayout")
        self.chatIn = QtWidgets.QLineEdit(self.chatInputWidget)
        self.chatIn.setObjectName("chatIn")
        self.chatInLayout.addWidget(self.chatIn)


        #Grid layout for the button
        self.btnGridWidget = QtWidgets.QWidget(self.centralwidget)
        self.btnGridWidget.setGeometry(QtCore.QRect(700, 500, 101, 71))
        self.btnGridWidget.setObjectName("btnGridWidget")
        self.btnGridLayout = QtWidgets.QGridLayout(self.btnGridWidget)
        self.btnGridLayout.setContentsMargins(0, 0, 0, 0)
        self.btnGridLayout.setObjectName("btnGridLayout")
        self.sendBtn = QtWidgets.QPushButton(self.btnGridWidget)
        self.sendBtn.setObjectName("sendBtn")
        self.sendBtn.clicked.connect(lambda: self.messageSend())
        self.btnGridLayout.addWidget(self.sendBtn, 0, 0, 1, 1)

        #Chat out layout
        self.chatOutputWidget = QtWidgets.QWidget(self.centralwidget)
        self.chatOutputWidget.setGeometry(QtCore.QRect(0, 0, 599, 490))
        self.chatOutputWidget.setObjectName("chatOutputWidget")
        self.chatOutLayout = QtWidgets.QHBoxLayout(self.chatOutputWidget)
        self.chatOutLayout.setContentsMargins(0, 0, 0, 0)
        self.chatOutLayout.setObjectName("chatOutLayout")
        self.chatOut = QtWidgets.QTextEdit(self.chatOutputWidget)
        
        #self.chatOut.setReadOnly(True)
        self.chatOut.setObjectName("chatOut")
        self.chatOutLayout.addWidget(self.chatOut)


        ChatWindow.setCentralWidget(self.centralwidget)

        #Menu bar
        self.menubar = QtWidgets.QMenuBar(ChatWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 21))
        self.menubar.setObjectName("menubar")

        #Menu file button
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        #Menu file action
        self.menuFile.triggered.connect(lambda: self._windowManager.guiEventHandler("OPEN_WINDOW_CONNECT"))
        ChatWindow.setMenuBar(self.menubar)


        self.statusbar = QtWidgets.QStatusBar(ChatWindow)
        self.statusbar.setObjectName("statusbar")
        ChatWindow.setStatusBar(self.statusbar)
        self.actionConnect = QtWidgets.QAction(ChatWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionExit = QtWidgets.QAction(ChatWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionConnect)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(ChatWindow)
        QtCore.QMetaObject.connectSlotsByName(ChatWindow)
        self.writeOut("Hello!")

    def retranslateUi(self, ChatWindow):
        _translate = QtCore.QCoreApplication.translate
        ChatWindow.setWindowTitle(_translate("ChatWindow", "PyChat - Disconnected"))
        self.sendBtn.setText(_translate("ChatWindow", "Send"))
        self.menuFile.setTitle(_translate("ChatWindow", "File"))
        self.actionConnect.setText(_translate("ChatWindow", "Connect"))
        self.actionExit.setText(_translate("ChatWindow", "Exit"))


    def openDialog(self, window):
        if(window == "connect"):
            print("WindowChat.py: Opening connection window")
            connectWindow = WindowConnect.WindowConnect(self._windowManager)
            connectWindow.show()

    def writeOut(self, message="", user="", **kwargs):

        additionString = ""

        if(kwargs != None):
            for v in kwargs:
                additionString = additionString + v + "=" + "'" + kwargs[v] + "' " 

        if(user != ""):
            toSend = "<font " + additionString + ">" + user + ": " + message + "</font>"
            print("WindowChat.py:", toSend)
            self.chatOut.append(toSend)
        else:
            toSend = "<font " + additionString + ">" + message + "</font>"
            self.chatOut.append(toSend)

    #Set a prefix for next chat out for the server to work with
    def prefixNextOut(self, prefix):
        self._prefixNext = True
        self._prefix = prefix

    def messageSend(self):
        userMessage = self.chatIn.text()

        if(userMessage != ""):
            if(self._prefixNext == True):
                userMessage = self._prefix + " " + userMessage
                self._windowManager.messageSend(userMessage)
                self.chatIn.clear()
                self.clearPrefix()
            else:
                self._windowManager.messageSend(userMessage)
                self.chatIn.clear()

    def updateClientList(self, clients):
        self.userModel.clear()
        users = clients.split()
        for user in users:
            item = QtGui.QStandardItem(user)
            item.setEditable = False
            self.userModel.appendRow(item)

    def clearPrefix(self):
        self._prefixNext = False
        self._prefix = ""
        
        
    def quit(self):
        sys.exit()