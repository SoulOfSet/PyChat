from netobj import Server
from db import DBManager

print("Welcome to PyChat\nJacob Sabella (SoulOfSet) - 2016\n")

#Initialize database
dbManager = DBManager.DbManager()
print(dbManager.checkDbExist())

#Create and start a new instance of the pychat Server netobj
print("Initialising server object")
server = Server.Server()
server.start()