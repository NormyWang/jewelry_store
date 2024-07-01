# app/routes/user_mutation.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user_model import UserModel
from app.schemas.user_schema import UserRegistrationSchema  # Added import for User
from app.database import get_db

user_mutation_router = APIRouter()

@user_mutation_router.post("/register", response_model=UserRegistrationSchema)
def register_user(user: UserRegistrationSchema, db: Session = Depends(get_db)):
    db_user = UserModel(
        username=user.username,
        password=user.password,
        email=user.email,
        address=user.address
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return User.from_orm(db_user)  # Changed to return User model instead of input schema