import sqlite3 as lite
import os.path
import os

class DbManager(object):

    def __init__(self):
        print("DbManager.py: DB Manager initialised")

    #Check fo existing db
    def checkDbExist(self):
        print(os.getcwd())
        return os.path.isfile("db/pychat.db")