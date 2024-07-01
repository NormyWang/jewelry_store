# app/schemas/product_schema.py
from pydantic import BaseModel
from typing import Optional

class ProductSchema(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: int
    quantity: int
    image_url: Optional[str]

    class Config:
        orm_mode = True