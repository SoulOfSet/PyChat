from threading import Thread

class Client(Thread):
    
    def __init__(self):
        super(Client, self).__init__()
        self.daemon = True;


        
    def run(self, conn, addr):
        conn.send(str.encode("Hello there\n"))
        while True:
            data = conn.recv(2048)
            print(data.decode('utf-8'), "\n")
            reply = "We got message: " + data.decode('utf-8') + "\n"
            
            if not data or data == "q":
                conn.sendall(str.encode("Goodbye"))
                print("Client from", addr[0], "has quit")
                break

            conn.sendall(str.encode(reply))
        conn.close()

    def cancel(self):
        """End this timer thread"""
        self.cancelled = True
