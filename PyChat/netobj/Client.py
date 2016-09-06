import socket
from netobj import ClientRecv, ClientSend

class Client(object):
    """Disposable client class"""
    _addr = ""
    _port = ""

    #Socket
    _s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _s.settimeout(1000)

    #Stop variable for client
    continueRunning = True;

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
        except:
            print("Client.py: Unable to connect")
            return False

    def run(self):
        x = ClientRecv.ClientRecv(self)
        x.start()
        y = ClientSend.ClientSend(self)
        y.start()
        while continueRunning:
            pass
