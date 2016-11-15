from threading import Thread

class ClientRecv(Thread):
    """Receiving thread for client"""

    _client = ""
    _recvCallback = ""
    _mainWindow = None

    def __init__(self, client, recvCallback=None):
        #Run the super class method so this runs as a thread
        Thread.__init__(self)
        self._client = client
        self._recvCallback = recvCallback
        self._mainWindow = self._client._window._mainWindow

    #Method ran when calling start()    
    def run(self):
        runRecv = True
        
        if(self._recvCallback == None): #Should be terminal
            while runRecv:
               data = self._client._s.recv(2048)
               print(data.decode("utf-8"), "\n")
        else: #Should be gui
            #The first bit of data that should be received from the server is an auth request
            receiver = self._client._s.recv(2048)
            if(receiver.decode("utf-8") == "CLIENT_AUTH_REQ"):

                #TODO: When done with localization class fix this
                print("ClientRecv.py: Server requires authentication")

                #Let the gui know that the server is now expecting a username from this location <3
                self._client.notifyGuiEvent("PROMPT_AUTH")

                #Authentication success/fail
                receiver = self._client._s.recv(2048)
                receiverSplit = receiver.decode().split()
                print(receiverSplit[0])

                if(receiver.decode("utf-8") == "CLIENT_REQ_NEW_USER"):
                    print("ClientRecv.py: Server does not recognize username. Prompt for new user")

                    #Let the chat window know were expecting some password data
                    self._client.notifyGuiEvent("REQ_NEW_USER_PASS")

                    receiver = self._client._s.recv(2048)
                    receiverSplit = receiver.decode().split()

                    if(receiver.decode("utf-8") == "CLIENT_AUTH_SUCC"):
                        print("ClientRecv.py: Client has authenticated with the server")
                        #Authentication was successfull. Run a consistent receive
                        while runRecv:
                            data = self._client._s.recv(2048)
                            print("ClientRecv.py", data.decode("utf-8"), "\n") 
                            if(data):
                                self._recvCallback(data.decode())

                    elif(receiverSplit[0] == "CLIENT_AUTH_FAIL"):
                        self._mainWindow.writeOut("Server refused auth with message: " + " ".join(receiverSplit[1:]), "", color="red")
                        self._mainWindow.writeOut("Disconnected from server", "", color="blue")
                        self._client.disconnect()

                elif((receiver.decode("utf-8") == "CLIENT_REQ_PASS")):
                    print("ClientRecv.py: Server has requested the users password since the user already exists in the database")

                    #Let the chat window know were sending out that password next 
                    self._client.notifyGuiEvent("CLIENT_REQ_PASS");

                    receiver = self._client._s.recv(2048)
                    receiverSplit = receiver.decode().split()

                    if(receiver.decode("utf-8") == "CLIENT_AUTH_SUCC"):
                        print("ClientRecv.py: Client has authenticated with the server")
                        #Authentication was successfull. Run a consistent receive
                        while runRecv:
                            data = self._client._s.recv(2048)
                            print("ClientRecv.py", data.decode("utf-8"), "\n") 
                            if(data):
                                self._recvCallback(data.decode())

                    elif(receiverSplit[0] == "CLIENT_AUTH_FAIL"):
                        self._mainWindow.writeOut("Server refused auth with message: " + " ".join(receiverSplit[1:]), "", color="red")
                        self._mainWindow.writeOut("Disconnected from server", "", color="blue")
                        self._client.disconnect()

                else:
                    #The server isn't functioning correctly
                    print("ClientRecv.py: Not receiving expected data from the server")

            else:
                print("ClientRecv.py: Not receiving expected data from the server")

            

    def cancel(self):
        """End this timer thread"""
        self.cancelled = True


