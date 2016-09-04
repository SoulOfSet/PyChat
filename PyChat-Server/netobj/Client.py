from threading import Thread
from netobj import ClientManager

class Client(Thread):
    
    _conn = "";
    _addr = "";

    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.daemon = True;
        self._conn = conn
        self._addr = addr
        
    def run(self):
        self._conn.send(str.encode("Hello there\n"))
        
        while True:
            data = self._conn.recv(2048)
            print(data.decode('utf-8'), "\n")
            reply = "We got message: " + data.decode('utf-8') + "\n"
            
            if not data or data == "q":
                self._conn.sendall(str.encode("Goodbye"))
                print("Client from", self._addr[0], "has quit")
                break

            self._conn.sendall(str.encode(reply))
        self._conn.close()

    def cancel(self):
        """End this timer thread"""
        self.cancelled = True


    def getAddress(self):
        return self._addr[0]