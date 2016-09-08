import tkinter as tk

class WindowConnect(tk.Frame):

    #Window manager
    _windowManager = ""
    #Labels
    _greetLabel = _addrLabel = _portLabel = _errorLabel = ""
    #Entries
    _addrEntry = _portEntry = ""
    #Buttons
    _connectButton = ""
    #Variable streams
    _errorText = _addrInput = _portInput = ""

    def __init__(self, windowManager):
        tk.Frame.__init__(self)

        #Let this window know who's boss
        self._windowManager = windowManager

        #Set the parent widget from the manager
        parentWidget = self._windowManager._rootWidget

        #Set up variable streams after tk init
        self._errorText = tk.StringVar()
        self._addrInput = tk.StringVar()
        self._portInput = tk.StringVar() 

        #Welcome label
        self._greetLabel = tk.Label(parentWidget, text="Welcome to PyChat", ).grid(row="0", column="0", columnspan="2", ipady="10")

        #Title for text inputs
        self._entryLabel = tk.Label(parentWidget, text="Enter the address and port you want to connect to").grid(row="1", column="0", columnspan="2", ipadx="3")

        #Entry/label for address
        self._addrLabel = tk.Label(parentWidget, text="Address").grid(row="2", column="0")
        self._addrEntry = tk.Entry(parentWidget, textvariable=self._addrInput).grid(row="2", column="1")
        
        #Entry for port
        self._portLabel = tk.Label(parentWidget, text="Port").grid(row="3", column="0", ipady="10")
        self._portEntry = tk.Entry(parentWidget, textvariable=self._portInput).grid(row="3", column="1")
        
        #Button
        self._connectButton = tk.Button(parentWidget, text="Connect", command=self.connect).grid(row="4", column="0", columnspan="2", ipady="5")

        #Label for errors
        self._errorLabel = tk.Label(parentWidget, textvariable=self._errorText).grid(row="5", column="0", columnspan="2", ipady="5")

    def connect(self):
        #Inform user of connection state
        print("Attempting to connect to", self._addrInput.get() + ":" + self._portInput.get())
        self._errorText.set("Connecting...")

        #Attempt connection
        connection = self._windowManager.connectClient(self._addrInput.get(), int(self._portInput.get()))
        if(connection == False):
             self._errorText.set("Connection Failed")
        else:
            self._errorText.set("Connected!")
        
    def quit(self):
        sys.exit()