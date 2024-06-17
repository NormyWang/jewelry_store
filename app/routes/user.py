from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.data import users
from app.models import User

router = APIRouter()

class UserRegistrationData(BaseModel):
    username: str
    password: str
    email: str
    address: str

class UserLoginData(BaseModel):
    username: str
    password: str

@router.post("/users/register")
async def register_user(user_data: UserRegistrationData):
    for user in users:
        if user.username == user_data.username:
            raise HTTPException(status_code=400, detail="Username already exists")
    new_user = User(user_data.username, user_data.password, user_data.email, user_data.address)
    users.append(new_user)
    return {"message": "User registered successfully"}

@router.post("/users/login")
async def login(user_data: UserLoginData):
    username = user_data.username
    password = user_data.password
    for user in users:
        if user.username == username and user.password == password:
            return {"access_token": "dummy_token", "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid username or password")