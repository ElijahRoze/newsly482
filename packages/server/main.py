import requests

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from .crawler import crawl_feeds
from .feed import CreateFeedRequest
from .user import LoginRequest
from .db import *

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:8080",
]

# Allow the website to make API calls
# without getting blocked from the browser.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/users/login")
async def handle_login(request: LoginRequest):
    error_msg = None
    try:
        # Try to login to the systsem through the database
        # if it fails, return an error message based on the type of failure
        if login(request.username, request.password):
            return {
                "msg": "Success"
            }
        else:
            error_msg = "Incorrect password"
    except Exception as e:
        error_msg = "User not found"
    
    # Return the error to the website if something happened
    raise HTTPException(status_code=400, detail=error_msg)

@app.get("/feeds")
async def list_feeds():
    try:
        return list_feed_sources()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Failed to create new feed")

@app.post("/feed")
async def create_feed(request: CreateFeedRequest):
    try:
        # Add the feed to the database
        return add_feed_source(request.feed_url)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Failed to create new feed")

@app.post("/users/create")
async def create(request: LoginRequest):
    try:
        # Attempt to create a new user
        return create_user(request.username, request.password)
    except:
        # If an error happened, assume the user already exists and return this
        raise HTTPException(status_code=400, detail="User already exists")


@app.post("/crawl")
async def crawl():
    try:
        # Call the "crawl_feeds" method to save all the articles to the database
        return crawl_feeds()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Failed to crawl feeds")

@app.get("/articles")
async def get_articles():
    try:
        # List all the news articles we have crawled.
        # TODO: generate a score specific to the current user
        # For now, we will show a random score, to demonstrate how it might work
        results = list_articles()
        results.sort(key=lambda x: -x['score'])
        return results
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Failed to retrieve articles")