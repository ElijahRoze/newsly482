from pymongo import MongoClient
import hashlib
from datetime import datetime

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)
db = client.newsly
client.admin.command("ping")

PWSALT = 'NeWsLyuWu!!'

def hash(password):
    return hashlib.md5((PWSALT + password).encode('utf-8')).hexdigest()

def save_news_article(title, url, model_inputs):
    already_indexed = db.news_articles.find_one({
        "url": url
    })

    if already_indexed:
        return

    return db.news_articles.insert_one({
        "title": title,
        "url": url,
        "model_inputs": model_inputs,
    })

def check_exists(username):
    # Potential issue: might be case sensitive
    return db.users.find_one({
        "username": username
    })

def add_feed_source(feed_url):
    feed_id = db.feed_sources.insert_one({
        "feed_url": feed_url,
    }).inserted_id

    return str(feed_id)

def list_feed_sources():
    sources = []
    cursor = db.feed_sources.find({})
    for source in cursor:
        sources.append({
            "feed_url": source['feed_url']
        })
    
    return sources

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

    if user == None:
        raise "User does not exist"
    
    return user["password"] == hash(password)


import random
def list_articles():
    articles = []
    cursor = db.news_articles.find({})
    for source in cursor:
        articles.append({
            "title": source['title'],
            "url": source['url'],
            "score": random.random(),
        })
    return articles