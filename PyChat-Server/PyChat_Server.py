from netobj import Server
from db import DbManager
import sys

print("Welcome to PyChat\nJacob Sabella (SoulOfSet) - 2016\n")

#Initialize database
dbManager = DbManager.DbManager()

#Check if database exists
if(dbManager.checkDbExist()):
    print("PyChat_Server.py: Existing database found")
    dbManager.connectToDb()
else:
    print("PyChat_Server.py: Database not found. Attempting creation")
    dbManager.createDatabase()
    

#Create and start a new instance of the pychat Server netobj
print("PyChat_Server.py: Initialising server object")
server = Server.Server(dbManager)
server.start()