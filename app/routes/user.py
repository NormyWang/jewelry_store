# app/routes/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import User as DBUser
from app.schemas import User, UserLogin  # Import the UserLogin schema
from app.database import get_db

router = APIRouter()

@router.post("/register", response_model=User)
def register_user(user: User, db: Session = Depends(get_db)):
    db_user = DBUser(username=user.username, password=user.password, email=user.email, address=user.address)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user

@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):  # Use the UserLogin schema
    db_user = db.query(DBUser).filter(DBUser.username == user_data.username, DBUser.password == user_data.password).first()
    if db_user is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"access_token": "dummy_token", "token_type": "bearer"}