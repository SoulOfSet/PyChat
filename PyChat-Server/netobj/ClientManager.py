from netobj import Client
import time

class ClientManager(object):
    _clientList = []


    def __init__(self):
        print("ClientManager.py: Client Manager initialised\n")

    def spawn_new_client(self, conn, addr):
        #Create a new client and pass the reference to this class
        client = Client.Client(conn, addr, self)

        #Add client class to list of clients
        self._clientList.append(client)

        #Begin that client's thread
        client.start()

    #String method for printing out the addresses of the clients
    def __str__(self):
        for x in self._clientList:
            return x.getAddress()

    #Sends message to all connected clients
    def broadcastText(self, message, user, type):
        for client in self._clientList:
            clientMessage = type + " " + user + " " + message
            client._conn.send(clientMessage.encode())

    #Send client list update package to all connected clients
    def broadcastClientList(self):
        #Build broadcast string
        clientList = ""
        for client in self._clientList:
            if(client._username != ""):
                clientList = clientList + " " + client._username

        self.broadcastText(clientList, "Server", "CLIENT_LIST")
