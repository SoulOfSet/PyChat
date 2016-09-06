from netobj import Client
import time

class ClientManager(object):
    _clientList = []

    data = "asdf"

    def __init__(self):
        print("ClientManager.py: Client Manager initialised\n")

    def spawn_new_client(self, conn, addr):
        #Create a new client and pass the reference to this class
        client = Client.Client(conn, addr, self)

        #Add client class to list of clients
        self._clientList.append(client)
        client.start()

    def __str__(self):
        for x in self._clientList:
            return x.getAddress()

    def broadcast(self, message):
        for client in self._clientList:
            client._conn.send(message.encode("utf-8"))