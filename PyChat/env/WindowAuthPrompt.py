import tkinter as tk

class WindowAuthPrompt(tk.Frame):

    #Window manager
    _windowManager = ""
    #Labels
    _greetLabel = _usernameLabel =  _infoLabel = ""
    #Entries
    _usernameEntry = _portEntry = ""
    #Buttons
    _loginButton = ""
    #Variable streams
    _infoText = _usernameInput = ""

    def __init__(self, parent, windowManager):
        tk.Frame.__init__(self, parent)

        #Let this window know who's boss
        self._windowManager = windowManager

        #Set the parent widget from the manager
        parentWidget = self._windowManager._rootWidget

        #Set up variable streams after tk init
        self._errorText = tk.StringVar()

        #Welcome label
        self._greetLabel = tk.Label(parentWidget, text="Enter Username").grid(row="0", column="0", columnspan="2", ipady="10")

        #Entry/label for address
        self._usernameLabel = tk.Label(parentWidget, text="Username").grid(row="1", column="0", ipady="10", ipadx="1")
        self._usernameEntry = tk.Entry(parentWidget, textvariable=self._usernameInput).grid(row="1", column="1", ipadx="1")
        
        #Button
        self._connectButton = tk.Button(parentWidget, text="Login", command=self.connect).grid(row="2", column="0", columnspan="2")

        #Label for info
        self._infoLabel = tk.Label(parentWidget, textvariable=self._infoText).grid(row="5", column="0", columnspan="2", ipady="5")
   
    def connect(self):
        #Inform user of connection state
        print("Attempting to connect to", self._usernameInput.get() + ":" + self._portInput.get())
        self._infoText.set("Connecting...")

        #Attempt connection
        connection = self._windowManager.connectClient(self._usernameInput.get(), int(self._portInput.get()))
        if(connection == False):
            self._infoText.set("Connection Failed")
        else:
            self._infoText.set("Connected!")
        
    def quit(self):
        sys.exit()