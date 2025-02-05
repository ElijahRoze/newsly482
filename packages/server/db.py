from pymongo import MongoClient
import hashlib

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)
db = client.newsly
client.admin.command("ping")

PWSALT = 'NeWsLyuWu!!'

def hash(password):
    return hashlib.md5((PWSALT + password).encode('utf-8')).hexdigest()

def check_exists(username):
    # Potential issue: might be case sensitive
    return db.users.find_one({
        "username": username
    })

def create_user(username, password):
    if check_exists(username):
        raise "User already exists"
    
    user_id = db.users.insert_one({
        "username": username,
        "password": hash(password),
    }).inserted_id

    return str(user_id)

def login(username, password):
    user = db.users.find_one({
        "username": username,
    })

    print(user)
    if user == None:
        raise "User does not exist"
    
    return user["password"] == hash(password)