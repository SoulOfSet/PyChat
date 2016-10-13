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

    #Sends message to particular user
    def sendPrivateMessage(self, message, userTo, userFrom):
        for client in self._clientList:
            if(userTo == client._username):
                if(userFrom == "SERVER"):
                    clientMessage = "TEXT " + userFrom + " " + message
                else:
                    clientMessage = "PM " + userFrom + " " + message 
                client._conn.send(clientMessage.encode())
                break
        print("ClientManager.py: User for private message not found")

    #Send client list update package to all connected clients
    def broadcastClientList(self):
        print("Broadcasting current client list")
        #Build broadcast string
        clientList = ""
        for client in self._clientList:
            if(client._username != ""):
                clientList = clientList + " " + client._username

        self.broadcastText(clientList, "SERVER", "CLIENT_LIST")

    #Remove a client
    def removeClient(self, conn):
        for client in self._clientList:
            if client._conn == conn:
                name = client._addr
                if(client._username != ""):
                    name = client._username
                print("ClientManager.py:", name, "has been removed from the client list")
                self._clientList.remove(client)
                self.broadcastClientList()
                break
