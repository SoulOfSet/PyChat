from threading import Thread

class ClientSend(Thread):
    """Sending thread for client"""

    _client = ""

    def __init__(self, client):
        #Run the super class method so this runs as a thread
        Thread.__init__(self)
        
        self._client = client

    #Method ran when calling start()    
    def run(self):
        runSend = True
        while runSend:
           userIn = input()
           self._client._s.send(userIn.encode("utf-8"))


    def cancel(self):
        """End this timer thread"""
        self.cancelled = True


