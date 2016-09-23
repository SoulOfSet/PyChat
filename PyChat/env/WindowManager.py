import sys
from netobj import GuiClient
from env import WindowChat
from env import WindowConnect
from PyQt5.QtWidgets import QApplication

class WindowManager(object):
    '''Centralised management for the application'''

    #Our connection to the server
    _connection = ""


    #The main "chat" window
    _mainWindow = ""

    

    def __init__(self):
        #Generate our QT inteface
        qApp = QApplication(sys.argv)
        self._mainWindow = WindowChat.WindowChat(self)
        #Show it
        self._mainWindow.show()
        qApp.exec_()
        
        

    def connectClient(self, addr, port):
        self._connection = GuiClient.GuiClient(self, self.messageRecv, addr, port)
        attempt = self._connection.connect()
        if(attempt == False):
            print("WindowManager.py: Unable to connect to server")
            return False
        else:
            print("WindowManager.py: Connection succeeded")
            self._connection.start()
            return True

    def messageRecv(self, message):
        print("wat")

    def guiEventHandler(self, event, **kwargs):
        print("WindowManager: Received GUI event", event)

        if(event == "OPEN_WINDOW_CONNECT"):
            print("WindowManager: Opening connection window")
            connectWindow = WindowConnect.WindowConnect(self)
            connectWindow.exec_()

        elif(event == "CLIENT_ATTEMPT_CONNECT"):
            print(kwargs)
            if(self.connectClient(kwargs.get("address"), int(kwargs.get("port")))):
                return True
            else:
                return False

        
        


