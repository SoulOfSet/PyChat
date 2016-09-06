import socket
from netobj import ClientRecv, ClientSend

class TerminalClient(object):
    """Disposable client class"""
    _addr = ""
    _port = ""

    #Socket
    _s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _s.settimeout(1000)

    #Stop variable for client
    _continueRunning = True;

    def __init__(self, addr="localhost", port=4500):
        self._addr = addr
        self._port = port
        print("Client.py: Client initialised with address", self._addr, "and port", self._port)

    def connect(self):
        try:
            print(self._addr, self._port)
            self._s.connect((self._addr, self._port))
            self.run()
            return True
        except socket.error as e:
            print(e)
            print("Client.py: Unable to connect to server")
            return False

    def run(self):
        x = ClientRecv.ClientRecv(self)
        x.start()
        y = ClientSend.ClientSend(self)
        y.start()
        while self._continueRunning:
            pass
