from threading import Thread

class ClientRecv(Thread):
    """Receiving thread for client"""

    _client = ""
    _recvCallback = ""

    def __init__(self, client, recvCallback=None):
        #Run the super class method so this runs as a thread
        Thread.__init__(self)
        self._client = client
        self._recvCallback = recvCallback

    #Method ran when calling start()    
    def run(self):
        runRecv = True
        
        if(self._recvCallback == None): #Should be terminal
            while runRecv:
               data = self._client._s.recv(2048)
               print(data.decode("utf-8"), "\n")
        else: #Should be gui
            #The first bit of data that should be received from the server is an auth request
            initialRecv = self._client._s.recv(2048)
            if(initialRecv.decode("utf-8") == "CLIENT_AUTH_REQ"):
                #TODO: When done with localization class fix this
                print("ClientRecv.py: CLIENT REQUEST USERNAME")

                #Let the gui know that the server is now expecting a username from this location <3
                self._client.notifyGuiEvent("PROMPT_AUTH")

                #Authentication success/fail
                initialRecv = self._client._s.recv(2048)
                if(initialRecv.decode("utf-8") == "CLIENT_AUTH_SUCC"):
                    print("ClientRecv.py: CLIENT AUTH SUCCESS")
                    #Authentication was successfull. Run a consistent receive
                    while runRecv:
                        data = self._client._s.recv(2048)
                        print(data.decode("utf-8"), "\n")
                        self._recvCallback(data.decode())
                else:
                    #The server isn't functioning correctly
                    print("ClientRecv.py: Not receiving expected data from the server")

            else:
                print("ClientRecv.py: Not receiving expected data from the server")

            

    def cancel(self):
        """End this timer thread"""
        self.cancelled = True


