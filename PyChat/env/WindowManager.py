import tkinter as tk
from env import WindowConnect
from env import WindowAuthPrompt
from netobj import GuiClient

class WindowManager(object):
    '''Centralised management for the application'''

    #Root tk widget
    _rootWidget = ""

    #Our connection to the server
    _connection = ""

    #Our window
    _window = ""

    def __init__(self):
        #Initialise tk
        self._rootWidget = tk.Tk()

        #Make a new instance of the connection window pane
        self._window = tk.Toplevel(self._rootWidget)
        connect = WindowConnect.WindowConnect(self._window)
        

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

    def guiEventHandler(self, event):
        print("WindowManager: Received GUI event", event)
        
        


