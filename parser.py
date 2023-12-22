from db import Database

db = Database()

read_data = open('Order 21506710.txt')

data = read_data.read()

lines = data.strip().split('\n')

parsed_data = []
test = []

for line in lines:
    elements = line.split('\t')
    parsed_data.append(elements)

for row in parsed_data:
    if row:
        name = row[0]
        birthday = row[1]
        email = row[2]
        password = row[3]
        photo_patch = row[8]
        test = row[9]
        db.connect()
        try:
            db.insert_users(name, birthday, email, password, photo_patch)
        finally:
            db.disconnect()

