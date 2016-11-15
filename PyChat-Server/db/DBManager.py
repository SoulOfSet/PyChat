import sqlite3 as lite
import os.path
import hashlib

class DbManager(object):

    #Database connection
    _dbConnection = None
    _cursor = None

    #SQL CONSTANTS
    SQL_USER_TABLE_MAKE = "CREATE TABLE Users (`id` int, `user` varchar(10), `pass` varchar(40), `accessLevel` int(2));"
    SQL_USER_INSERT_ADMIN = "INSERT INTO Users (`id`, `user`, `pass`, `accessLevel`) VALUES (1, 'admin', 'd033e22ae348aeb5660fc2140aec35850c4da997', 0);"
    SQL_USER_TABLE_COUNT = "SELECT COUNT(*) FROM Users;"

    def __init__(self):
        print("DbManager.py: Database Manager initialised")

    #Check for existing db
    def checkDbExist(self):
        print("DbManager.py: Checking for existing database")
        return os.path.isfile("db/pychat.db")

    #Create database
    def createDatabase(self):
        print("DbManager.py: Attempting to create PyChat database")
        try:
            self._dbConnection = lite.connect("db/pychat.db", check_same_thread = False)
            self._cursor = self._dbConnection.cursor()
            self.setupTable()
            return True
        except lite.Error as e:
            print("DbManager.py: Unable to create database. Error: " + e)
            return False

    #Connect to database
    def connectToDb(self):
        try:
            self._dbConnection = lite.connect("db/pychat.db", check_same_thread = False)
            self._cursor = self._dbConnection.cursor()
            print("DbManager.py: Successfully connected to existing database")
            return True
        except lite.Error as e:
            print("DbManager.py: Unable to connect to database. Error: " + e)
            return False

    #Set up database tables
    def setupTable(self):
        print("DbManager.py: Attempting to set up user table")
        try:
            self._cursor.execute(self.SQL_USER_TABLE_MAKE)
            self._cursor.execute(self.SQL_USER_INSERT_ADMIN)
            self._dbConnection.commit()
            print("DbManager.py: User table set up complete")
            print("DbManager.py: Login with username admin and password admin to edit configration")
        except lite.Error as e:
            print("DbManager.py: Unable to set up user table with error: " + e)
            return False

    #Authenticate username and password
    def authenticateUser(self, user, password):
        print("DbManager.py: Attemping to authenticate user " + user)
        hashPass = hashlib.sha1(password).hexdigest()
        try:
            self._cursor.execute("SELECT pass, accessLevel FROM Users WHERE user = :user", {'user': user})
        except lite.Error as e:
            print("DbManager.py: Unable to query for user with error:", e)

        rows = self._cursor.fetchall()

        #Raise exception if user does not exist
        if(len(rows) < 1):
            return False

        #Authentication is a success
        if(rows[0][0] == hashPass):
            
            print("DbManager.py: User " + user + " passed authentication")
            return True
        #Authentication is a fail
        else:
            print("DbManager.py: User " + user + " failed authentication")
            return False

    #Check if a user exists
    def checkUserExist(self, user):
        print("DbManager.py: Attempting to check for user", user)

        try:
            self._cursor.execute("SELECT user FROM Users WHERE user = :user", {'user': user})
        except lite.Error as e:
            print("DbManager.py: Unable to query for user with error:", e)

        rows = self._cursor.fetchall()

        if(len(rows) < 1):
            print("DbManager.py: User", user, "does not exist in the database")
            return False
        else:
            print("DbManager.py: User", user, "was found in the database")
            return True

    def getNumUsers(self):
        self._cursor.execute(self.SQL_USER_TABLE_COUNT)
        result = self._cursor.fetchone()
        return result[0];

    def addUser(self, username, password):
        print("Attempting to add user", username, "to the database")
        hashPass = hashlib.sha1(password)
        userId = self.getNumUsers() + 1
        self._cursor.execute("INSERT INTO Users (`id`, `user`, `pass`, `accessLevel`) VALUES(?, ?, ?, 3);", (userId, username, hashPass.hexdigest()))  
        self._dbConnection.commit()

