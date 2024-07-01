# app/routes/order_mutation.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.models.order_model import OrderModel
from app.models.product_model import ProductModel
from app.schemas.order_schema import OrderSchema
from app.database import get_db

order_mutation_router = APIRouter()

@order_mutation_router.post("/", response_model=OrderSchema)
def create_order(order: OrderSchema, db: Session = Depends(get_db)):
    db_order = OrderModel(user_id=order.user_id, order_date=datetime.utcnow())
    for product in order.products:
        db_product = ProductModel(**product.dict())
        db.add(db_product)
        db_order.products.append(db_product)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return order