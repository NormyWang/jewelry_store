# app/routes/product.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models import Product as DBProduct
from app.schemas import Product
from app.database import get_db  # Import the get_db dependency

router = APIRouter()

@router.get("/", response_model=List[Product])
def list_products(db: Session = Depends(get_db)):
    products = db.query(DBProduct).all()
    return products

@router.get("/search")
def search_products(query: str, db: Session = Depends(get_db)):
    products = db.query(DBProduct).filter(DBProduct.name.ilike(f"%{query}%") | DBProduct.description.ilike(f"%{query}%")).all()
    return products

@router.post("/", response_model=Product)
def create_product(product: Product, db: Session = Depends(get_db)):
    db_product = DBProduct(name=product.name, description=product.description, price=product.price,
                         quantity=product.quantity, image_url=product.image_url)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return product