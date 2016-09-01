from netobj import Client

class ClientManager:

    _clientList = []

    def __init__(self):
        print("ClientManager.py: Client Manager initialised\n")

    def spawn_new_client(self, conn, addr):
        client = Client.Client()
        self._clientList[(addr[0], + ":", str(addr[1]))] = client

    def __str__(self):
        for x in self._clientList:
            print(x)