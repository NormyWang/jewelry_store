# app/routes/order_getter.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.order_model import OrderModel
from app.schemas.order_schema import OrderSchema
from app.database import get_db

order_getter_router = APIRouter()

# Add getter functions here if needed