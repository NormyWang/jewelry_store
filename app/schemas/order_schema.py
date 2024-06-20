# app/schemas/order_schema.py
from pydantic import BaseModel
from typing import List
from datetime import datetime
from app.schemas.product_schema import Product

class Order(BaseModel):
    order_id: int
    user_id: int
    order_date: datetime
    products: List[Product]

    class Config:
        orm_mode = True