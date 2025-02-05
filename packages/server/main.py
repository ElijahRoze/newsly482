from fastapi import FastAPI, HTTPException

from .user import LoginRequest
from .db import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/users/login")
async def handle_login(request: LoginRequest):
    error_msg = None
    try:
        if login(request.username, request.password):
            return True
        else:
            error_msg = "Incorrect password"
    except Exception as e:
        error_msg = "User not found"
    
    raise HTTPException(status_code=400, detail=error_msg)


@app.post("/users/create")
async def create(request: LoginRequest):
    try:
        return create_user(request.username, request.password)
    except:
        raise HTTPException(status_code=400, detail="User already exists")