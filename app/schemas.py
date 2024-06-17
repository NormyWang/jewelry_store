from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Pydantic model for User
class User(BaseModel):
    username: str
    email: Optional[str]
    address: Optional[str]
    password: str
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str
    
# Pydantic model for Product
class Product(BaseModel):
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
