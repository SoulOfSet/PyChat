from threading import Thread
from netobj import ClientManager

class Client(Thread):
    _conn = ""
    _addr = ""
    _manager = ""
    _username = ""


    def __init__(self, conn, addr, manager):

        #Run the super class method so this runs as a thread
        Thread.__init__(self)

        #Run thread as a daemon so it dies when the main thread does
        self.daemon = True;

        #Set own connection method and address
        self._conn = conn
        self._addr = addr

        #Reference to the instace of our server manager class
        self._manager = manager
    
    #Method ran when calling start()    
    def run(self):
        #Ask user for atuh details
        self._conn.send(str.encode("CLIENT_AUTH_REQ"))

        authenticated = False 

        while(authenticated == False):
            #Get the username for the user
            try:
                username = self._conn.recv(2048)
            except (ConnectionResetError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError):
                print("Client.py: Client with IP", self._addr, "failed to hold connection")
                self._manager.removeClient(self._conn)
                self.cancel()
                break

            username = username.decode('utf-8')

            #Split username string
            unameSplit = username.split()

            #Look for uname prefix
            if(unameSplit[0] == "UNAME"):
                failReason = ""
                #Make sure its not empty
                if(unameSplit[1] == "" or len(unameSplit[1]) < 3):
                    print("Client.py: Invalid length for username")
                    failReason = "Username must be more than 3 characters"
                
                
                #If there is a failiure inform the client with the reason
                if(failReason != ""):
                    self._conn.send(str.encode("CLIENT_AUTH_FAIL" + " " + failReason))
                else:
                    self._username = unameSplit[1]
                    authenticated = True
                    self._conn.send(str.encode("CLIENT_AUTH_SUCC"))
                    self._manager.sendPrivateMessage("Welcome " + self._username, self._username, "SERVER")
            else:
                self._conn.send(str.encode("CLIENT_AUTH_FAIL"))

        self._manager.broadcastClientList()
        #Loop for receiving messages on this thread
        while True and authenticated:
            #Data received. Must be decoded from byte string to string
            try:
                data = self._conn.recv(2048)
            except (ConnectionResetError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError):
                print("Client.py:", self._username, "has dropped the connection")
                self._manager.removeClient(self._conn)
                self.cancel()
                break
            print("TEXT" + " " + self._username + ": " + data.decode('utf-8'))
            reply = data.decode('utf-8')
            
            if not data:
                print("Client from", self._addr[0], "has quit")
                break

            self._manager.broadcastText(reply, self._username, "TEXT")
        self._conn.close()

    def cancel(self):
        """End this timer thread"""
        self.cancelled = True

    def getAddress(self):
        return self._addr[0]