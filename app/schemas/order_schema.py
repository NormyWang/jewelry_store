# app/schemas/order_schema.py
from pydantic import BaseModel
from typing import List
from datetime import datetime
from app.schemas.product_schema import ProductSchema

class OrderSchema(BaseModel):
    order_id: int
    user_id: int
    order_date: datetime
    products: List[ProductSchema]

    class Config:
        orm_mode = True