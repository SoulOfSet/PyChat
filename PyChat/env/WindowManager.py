import sys
from netobj import GuiClient
from env import WindowChat
from PyQt5.QtWidgets import QApplication

class WindowManager(object):
    '''Centralised management for the application'''

    #Our connection to the server
    _connection = ""

    def __init__(self):
        qApp = QApplication(sys.argv)
        mainWindow = WindowChat.WindowChat()
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

    def guiEventHandler(self, event):
        print("WindowManager: Received GUI event", event)

        
        


