from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Pydantic model for User
class User(BaseModel):
    id: int
    username: str
    email: str
    address: Optional[str]

    class Config:
        orm_mode = True

# Pydantic model for Product
class Product(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: int
    quantity: int
    image_url: Optional[str]

    class Config:
        orm_mode = True

# Pydantic model for Order
class Order(BaseModel):
    order_id: int
    user_id: int
    order_date: datetime
    products: List[Product]

    class Config:
        orm_mode = True
