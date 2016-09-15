import socket
from threading import Thread
from netobj import ClientRecv

class GuiClient(Thread):

    """Disposable client class"""
    _addr = ""
    _port = ""

    #Socket
    _s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _s.settimeout(1000)

    #Stop variable for client
    _continueRunning = True;

    #Window manager
    _window = ""

    #recv event callback
    _recvCallback = ""

    def __init__(self, manager, recvCallback, addr="localhost", port=4500):

        #Run the super class method so this runs as a thread
        Thread.__init__(self)

        #Set locals
        self._addr = addr
        self._port = port
        self._window = manager
        self._recvCallback = recvCallback

        print("GuiClient.py: Client initialised with address", self._addr, "and port", self._port)

    #Attempt client server connection
    def connect(self):
        print("GuiClient.py: Attempting connection")
        try:
            #Use our socket to try to connect
            print(self._addr, self._port)
            self._s.connect((self._addr, self._port))
            return True
        except socket.error as e:
            print(e)
            print("GuiClient.py: Unable to connect to server")
            return False

    #The receive thread for getting data sent asynchronously
    def run(self):
        print("GuiClient.py: Running receive server")
        #Run receive thread with callback needed to get data
        clientRecv = ClientRecv.ClientRecv(self, self._recvCallback)
        clientRecv.start()

    def cancel(self):
        """End this timer thread"""
        self.cancelled = True

    def notifyGuiEvent(self, event):
        print("GuiClient.py: Received GUI event", event + ".", "Forwading to window manager")
        #Send event to window manager handler
        self._window.guiEventHandler(event)