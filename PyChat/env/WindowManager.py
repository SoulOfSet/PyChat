import tkinter as tk
from env import WindowConnect
from netobj import GuiClient

class WindowManager(object):
    '''Centralised management for the application'''

    _rootWidget = ""

    #Our connection to the server
    _connection = ""

    def __init__(self):
        self._rootWidget = tk.Tk("PyChat")
        WindowConnect.WindowConnect(self)
        
    def run(self):
        self._rootWidget.mainloop()

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
    


