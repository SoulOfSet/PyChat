from threading import Thread

class ClientRecv(Thread):
    """Receiving thread for client"""

    _client = ""
    _callback = ""

    def __init__(self, client, callback=None):
        #Run the super class method so this runs as a thread
        Thread.__init__(self)
        self._client = client
        self._callback = callback

    #Method ran when calling start()    
    def run(self):
        runRecv = True
        if(self._callback == None):
            while runRecv:
               data = self._client._s.recv(2048)
               print(data.decode("utf-8"), "\n")
        else:
            while runRecv:
               data = self._client._s.recv(2048)
               print(data.decode("utf-8"), "\n")
               self._callback(data.decode())

    def cancel(self):
        """End this timer thread"""
        self.cancelled = True


