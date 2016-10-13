import sys
from netobj import GuiClient
from env import WindowChat, WindowConnect, WindowAuth
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
        
        
    #Bind clinet to socket server
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

    #On message receive
    def messageRecv(self, message):
        #Split message
        messageSplit = message.split()

        #Message out from server
        if(messageSplit[0] == "TEXT"):
            #Determine if its a server or user message
            if(messageSplit[1] != "SERVER"):
                self._mainWindow.writeOut(" ".join(messageSplit[2:]), messageSplit[1])
            else:
                self._mainWindow.writeOut(" ".join(messageSplit[2:]), "Server", color="blue")

        elif(messageSplit[0] == "CLIENT_LIST"):
            self._mainWindow.updateClientList(" ".join(messageSplit[2:]))

    #On message send
    def messageSend(self, message):
        self._connection.messageSend(message)

    def guiEventHandler(self, event, **kwargs):
        print("WindowManager: Received GUI event", event)

        if(event == "OPEN_WINDOW_CONNECT"):
            print("WindowManager: Asking main window to open connect dialog")
            self._mainWindow.openDialog("connect")

        elif(event == "CLIENT_ATTEMPT_CONNECT"):
            print(kwargs)
            if(self.connectClient(kwargs.get("address"), int(kwargs.get("port")))):
                return True
            else:
                return False

        elif(event == "PROMPT_AUTH"):
            print("WindowManager.py: Prompt for username")
            print("WindowManager.py: Prefixing next output for server with UNAME")
            self._mainWindow.prefixNextOut("UNAME")
            self._mainWindow.writeOut("Enter your username:", "", color="red")
            

        
        


