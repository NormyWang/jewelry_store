# app/routes/__init__.py
from fastapi import APIRouter
from .user_getter import user_getter_router
from .user_mutation import user_mutation_router
from .order_getter import order_getter_router
from .order_mutation import order_mutation_router
from .product_getter import product_getter_router
from .product_mutation import product_mutation_router

main_router = APIRouter()

main_router.include_router(user_getter_router, prefix="/users", tags=["users"])
main_router.include_router(user_mutation_router, prefix="/users", tags=["users"])
main_router.include_router(order_getter_router, prefix="/orders", tags=["orders"])
main_router.include_router(order_mutation_router, prefix="/orders", tags=["orders"])
main_router.include_router(product_getter_router, prefix="/products", tags=["products"])
main_router.include_router(product_mutation_router, prefix="/products", tags=["products"])