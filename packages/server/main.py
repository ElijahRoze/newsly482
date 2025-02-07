from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .user import LoginRequest
from .db import *

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:8080",
]
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
        if login(request.username, request.password):
            return {
                "msg": "Success"
            }
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