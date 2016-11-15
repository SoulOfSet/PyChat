import socket
from netobj import ClientManager

class Server(object):
    'The Server object'

    #Define our address an port variable for the socket to bind to
    _addr = ""
    _port = ""
    
    #Database manager
    _dbManager = None

    #Client manager declaration
    _clientManager = None

    #Define a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Constructor with default values for address and port
    def __init__(self, dbManager, addr="localhost", port=4500):
        self._addr = addr
        self._port = port
        self._dbManager = dbManager

        #Create a new instance of the client manager
        self._clientManager = ClientManager.ClientManager(self)

    #Start method that binds the server
    def start(self):
        #Attempt the bind
        try:
            self.s.bind((self._addr, self._port))
        #Unable to bind
        except socket.error as e:
            print(str(e))

        #Begin listening
        self.s.listen(10)

        #Let the user know the address and port the server is bound to
        print("Server.py: Server started on address", self._addr, "on port", self._port)

        while True:
            conn, addr = self.s.accept()
            print('Server.py: Client incoming connection from address '+addr[0]+':'+str(addr[1]))
            self._clientManager.spawn_new_client(conn, addr)