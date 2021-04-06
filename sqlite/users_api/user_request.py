from users_db import UserDB
import requests

r = requests.get('https://jsonplaceholder.typicode.com/users')
users = r.json()

user_db = UserDB()
user_db.create_connection()

for user in users:
    name = user['name']
    username = user['username']
    city = user['address']['city']
    zipcode = user['address']['zipcode']
    user_db.add_one(name, username, city, zipcode)

user_db.close_conn()

