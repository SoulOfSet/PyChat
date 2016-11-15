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

        authenticated = False 

        while(authenticated == False):
            #Ask user for auth details
            self._conn.send(str.encode("CLIENT_AUTH_REQ"))

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
                if(unameSplit[1] == "" or len(unameSplit[1]) < 3 or len(unameSplit[1]) > 10):
                    print("Client.py: Invalid length for username")
                    self._conn.send(str.encode("CLIENT_AUTH_FAIL" + " " + "Username must be more than 3 characters and less then ten"))
                    break

                elif(self._manager._server._dbManager.checkUserExist(unameSplit[1])):
                     print("Client.py: User", unameSplit[1], "exists in the database")

                     while True:
                        #This user exists. Ask for the password
                        self._conn.send(str.encode("CLIENT_REQ_PASS"))
                        try:
                            passwordString = self._conn.recv(2048)
                            passwordString = passwordString.decode()
                        except (ConnectionResetError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError):
                            print("Client.py: Client with IP", self._addr, "failed to hold connection")
                            self._manager.removeClient(self._conn)
                            self.cancel()
                            break
                        
                        #Compare the two passwords and make sure theyre identical
                        passSplit = passwordString.split()
                        if(passSplit[0] == "PASS"):
                            print(self._manager._server._dbManager.authenticateUser(unameSplit[1], passSplit[1].encode()))
                            if(self._manager._server._dbManager.authenticateUser(unameSplit[1], passSplit[1].encode()) == False):
                                self._conn.send(str.encode("CLIENT_AUTH_FAIL" + " " + "Authentication failed with given password"))
                            else:
                                self._username = unameSplit[1]
                                self._conn.send(str.encode("CLIENT_AUTH_SUCC"))
                                self._manager.sendPrivateMessage("Welcome " + self._username, self._username, "SERVER")
                                authenticated = True
                                break

                elif(self._manager._server._dbManager.checkUserExist(unameSplit[1]) == False):
                    print("Client.py: User", unameSplit[1], "does not exist in the database")

                    while True:
                        #Ask the user if they want to make this an account
                        self._conn.send(str.encode("CLIENT_REQ_NEW_USER"))
                        try:
                            passwordString = self._conn.recv(2048)
                            passwordString = passwordString.decode()
                        except (ConnectionResetError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError):
                            print("Client.py: Client with IP", self._addr, "failed to hold connection")
                            self._manager.removeClient(self._conn)
                            self.cancel()
                            break
                        
                        #Compare the two passwords and make sure theyre identical
                        passSplit = passwordString.split()
                        if(passSplit[0] == "PASS"):
                            if(passSplit[1] != passSplit[2]):
                                self._conn.send(str.encode("CLIENT_AUTH_FAIL" + " " + "Passwords did not match"))
                            else:
                                self._manager._server._dbManager.addUser(unameSplit[1], passSplit[1].encode())
                                self._username = unameSplit[1]
                                self._conn.send(str.encode("CLIENT_AUTH_SUCC"))
                                self._manager.sendPrivateMessage("Welcome " + self._username, self._username, "SERVER")
                                authenticated = True
                                break

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