# app/routes/user_getter.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user_model import UserModel
from app.schemas.user_schema import UserLoginSchema
from app.database import get_db

user_getter_router = APIRouter()

@user_getter_router.post("/login")
def login(user_data: UserLoginSchema, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(
        UserModel.username == user_data.username,
        UserModel.password == user_data.password
    ).first()
    if db_user is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"access_token": "dummy_token", "token_type": "bearer"}