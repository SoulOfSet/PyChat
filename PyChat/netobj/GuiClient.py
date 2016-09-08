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

    #recv even callback
    _recvCallback = ""

    def __init__(self, manager, recvCallback, addr="localhost", port=4500):

        #Run the super class method so this runs as a thread
        Thread.__init__(self)

        self._addr = addr
        self._port = port
        self._window = manager
        self._recvCallback = recvCallback

        print("GuiClient.py: Client initialised with address", self._addr, "and port", self._port)

    def connect(self):
        print("GuiClient.py: Attempting connection")
        try:
            print(self._addr, self._port)
            self._s.connect((self._addr, self._port))
            return True
        except socket.error as e:
            print(e)
            print("GuiClient.py: Unable to connect to server")
            return False

    def run(self):
        print("GuiClient.py: Running receive server")
        clientRecv = ClientRecv.ClientRecv(self, self._recvCallback)
        clientRecv.start()
        while(self._continueRunning):
            pass

    def cancel(self):
        """End this timer thread"""
        self.cancelled = True