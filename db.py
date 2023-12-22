import mysql.connector

class Database:
    def __init__(self):
        self.cursor = None
        self.connection = None
    def connect(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='myuser',
            password='mypassword',
            database='mydatabase'
        )
        self.cursor = self.connection.cursor()