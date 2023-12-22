import mysql.connector

class Database:
    def __init__(self):
        self.cursor = None
        self.connection = None
    def connect(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='massag_Bot',
            port=3307
        )
        self.cursor = self.connection.cursor()
        
    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            
    def insert_users(self, name, birthday, email, password, photo_patch):
        with self.connection:
            self.cursor.execute(
                "insert into clients (client_id, name, lang, birthday, email, password, photo_patch) values (1212, %s, 'ru', %s, %s, %s, %s)",
                (name, birthday, email, password, photo_patch))
            self.connection.commit()
            self.cursor.close()