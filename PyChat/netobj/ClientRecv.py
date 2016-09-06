from threading import Thread

class ClientRecv(Thread):
    """Receiving thread for client"""

    _client = ""

    def __init__(self, client):
        #Run the super class method so this runs as a thread
        Thread.__init__(self)

        
        self._client = client

    #Method ran when calling start()    
    def run(self):
        runRecv = True
        while runRecv:
           data = self._client._s.recv(2048)
           print(data.decode("utf-8"), "\n")


    def cancel(self):
        """End this timer thread"""
        self.cancelled = True


