# app/routes/order.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.models import Order as DBOrder, Product as DBProduct
from app.schemas import Order
from app.database import get_db  # Import the get_db dependency

router = APIRouter()

@router.post("/", response_model=Order)
def create_order(order: Order, db: Session = Depends(get_db)):
    db_order = DBOrder(user_id=order.user_id, order_date=datetime.utcnow())
    for product in order.products:
        db_product = DBProduct(**product.dict())
        db.add(db_product)
        db_order.products.append(db_product)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return order