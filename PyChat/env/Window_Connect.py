import tkinter as tk

class Window_Connect(tk.Frame):

    def __init__(self, parent, connectCallback):
        tk.Frame.__init__(self, parent)
        #Welcome label
        greetLabel = tk.Label(parent, text="Welcome to PyChat", ).grid(row="0", column="0", columnspan="2", ipady="10")

        #Title for text inputs
        entryLabel = tk.Label(parent, text="Enter the address and port you want to connect to").grid(row="1", column="0", columnspan="2", ipadx="3")

        #Entry/label for address
        addrLabel = tk.Label(parent, text="Address").grid(row="2", column="0")
        addrEntry = tk.Entry(parent).grid(row="2", column="1")
        
        #Entry for port
        portLabel = tk.Label(parent, text="Port").grid(row="3", column="0", ipady="10")
        portEntry = tk.Entry().grid(row="3", column="1")
        
        #Button
        connectButton = tk.Button(parent, text="Connect", command=self.swag).grid(row="4", column="0", columnspan="2", ipady="5")

    def swag(self):
        print("Swag")

    def quit(self):
        sys.exit()