from threading import Thread
from netobj import ClientManager

class Client(Thread):
    _conn = ""
    _addr = ""
    _manager = ""
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
        #Greet the user
        self._conn.send(str.encode("#0000\n"))

        #Loop for receiving messages on this thread
        while True:
            #Data received. Must be decoded from byte string to string
            data = self._conn.recv(2048)
            print(data.decode('utf-8'), "\n")
            reply = data.decode('utf-8')
            
            if not data:
                print("Client from", self._addr[0], "has quit")
                break

            self._manager.broadcast(reply)
        self._conn.close()

    def cancel(self):
        """End this timer thread"""
        self.cancelled = True

    def getAddress(self):
        return self._addr[0]