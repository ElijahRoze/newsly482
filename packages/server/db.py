from pymongo import MongoClient
import hashlib


uri = "mongodb://localhost:27017/"
client = MongoClient(uri)
db = client.newsly
client.admin.command("ping")

# Salt the password so it is safe from a rainbow table attack
PWSALT = 'NeWsLyuWu!!'

def hash(password):
    return hashlib.md5((PWSALT + password).encode('utf-8')).hexdigest()

def check_exists(username):
    # Potential issue: might be case sensitive
    return db.users.find_one({
        "username": username
    })

def create_user(username, password):
    # When creating a user, check if the user exists. If they do
    # then raise an exception
    if check_exists(username):
        raise "User already exists"

    # Insert the new user into the database
    user_id = db.users.insert_one({
        "username": username,
        "password": hash(password),
    }).inserted_id

    # Return the user id
    return str(user_id)

def login(username, password):
    # Lookup the user by the username
    user = db.users.find_one({
        "username": username,
    })

    # If the user does not exist, return an error
    if user is None:
        raise "User does not exist"

    # Otherwise, return true if the password matches or false if it doesn't
    return user["password"] == hash(password)