# app/routes/product_mutation.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.product_model import ProductModel
from app.schemas.product_schema import ProductSchema
from app.database import get_db

product_mutation_router = APIRouter()

@product_mutation_router.post("/", response_model=ProductSchema)
def create_product(product: ProductSchema, db: Session = Depends(get_db)):
    db_product = ProductModel(
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity,
        image_url=product.image_url
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return product