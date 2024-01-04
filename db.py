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
        def insert_user(self, user_id):
        with self.connection:
            self.cursor.execute(
                # "insert into users (user_id, first_name, last_name, surname, photo_path, client_id) values (%s, 'gfgf', 'gfgf', 'gfgf', 'gfgf', 1) ",
                # (user_id,))
                "insert into users (user_id) values (%s) ",
                (user_id,))
            self.connection.commit()
            self.cursor.close()

    def exit_user(self, user_id):
        with self.connection:
            self.cursor.execute("select * from users where user_id = %s", (user_id,))
            result = self.cursor.fetchall()
            return bool(result)

    def get_lang(self, user_id):
        with self.connection:
            self.cursor.execute("select lang from users where user_id = %s", (user_id,))
            result = self.cursor.fetchone()
            return result[0]

    def set_lang(self, user_id, lang):
        with self.connection:
            self.cursor.execute("UPDATE users SET lang = %s WHERE user_id = %s", (lang, user_id,))
            self.connection.commit()
            self.cursor.close()

    def user_by_client_id(self, user_id):
        with self.connection:
            self.cursor.execute("select * from clients where client_id = %s", (user_id,))
            return self.cursor.fetchone()[0]

    async def insert_state(self, state: FSMContext, incoming_message_id, name_field):
        user_state_data = {'message_id': incoming_message_id.message_id}
        await state.update_data({name_field: user_state_data})

    async def get_state(self, state: FSMContext, name_field):
        user_state_data: dict = await state.get_data()
        result = user_state_data.get(name_field)
        return result['message_id']
