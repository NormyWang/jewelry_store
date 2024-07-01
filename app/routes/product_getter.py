# app/routes/product_getter.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models.product_model import ProductModel
from app.schemas.product_schema import ProductSchema
from app.database import get_db

product_getter_router = APIRouter()

@product_getter_router.get("/", response_model=List[ProductSchema])
def list_products(db: Session = Depends(get_db)):
    products = db.query(ProductModel).all()
    return products

@product_getter_router.get("/search")
def search_products(query: str, db: Session = Depends(get_db)):
    products = db.query(ProductModel).filter(
        ProductModel.name.ilike(f"%{query}%") | 
        ProductModel.description.ilike(f"%{query}%")
    ).all()
    return products