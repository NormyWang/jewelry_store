# app/schemas/user_schema.py
from pydantic import BaseModel
from typing import Optional

class UserRegistrationSchema(BaseModel):
    username: str
    email: Optional[str]
    address: Optional[str]
    password: str
    class Config:
        orm_mode = True

class UserLoginSchema(BaseModel):
    username: str
    password: str