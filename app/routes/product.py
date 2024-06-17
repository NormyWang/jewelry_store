from fastapi import APIRouter
from app.data import products  # Assuming products is correctly imported and initialized in data.py
from app.models import Product  # Import the Product class

router = APIRouter()

@router.get("/")
async def list_products():
    return [product.__dict__ for product in products]

@router.get("/search")
async def search_products(query: str):
    result = [product.__dict__ for product in products if query.lower() in product.name.lower() or query.lower() in product.description.lower()]
    return result
