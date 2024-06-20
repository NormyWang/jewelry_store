# app/schemas/user_schema.py
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    email: Optional[str]
    address: Optional[str]
    password: str
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str