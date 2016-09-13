import tkinter as tk
from env import WindowConnect
from netobj import GuiClient

class WindowManager(object):
    '''Centralised management for the application'''

    #Root tk widget
    _rootWidget = ""

    #Our connection to the server
    _connection = ""

    def __init__(self):
        #Initialise tk
        self._rootWidget = tk.Tk("PyChat")

        #Make a new instance of the connection window pane
        WindowConnect.WindowConnect(self)
        
    def run(self):
        #Run the tk look
        self._rootWidget.mainloop()

    #Connect client to server
    def connectClient(self, addr, port):
        #Gui Client insance. Store it
        self._connection = GuiClient.GuiClient(self, self.messageRecv, addr, port)

        #Make a connection attempt
        attempt = self._connection.connect()

        #Check if successful
        if(attempt == False):
            print("WindowManager.py: Unable to connect to server")
            return False
        else:
            print("WindowManager.py: Connection succeeded")
            #Begin the receive thread for the server data
            self._connection.start()
            return True

    #Method for dealing with data. Used as a callback
    def messageRecv(self, message):
        print(message)
    


