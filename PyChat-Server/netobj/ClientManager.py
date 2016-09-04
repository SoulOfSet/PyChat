from netobj import Client

class ClientManager(object):

    _clientList = []

    def __init__(self):
        super(ClientManager, self).__init__()
        print("ClientManager.py: Client Manager initialised\n")

    def spawn_new_client(self, conn, addr):
        client = Client.Client(conn, addr)
        self._clientList.append(client)
        client.start()

    def killerSwag(self):
        print("swag")

    def __str__(self):
        for x in self._clientList:
            return x.getAddress()