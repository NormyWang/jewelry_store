# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import route files
from app.routes.user import router as user_router
from app.routes.product import router as product_router
from app.routes.order import router as order_router

# FastAPI app
app = FastAPI()

# CORS configuration
origins = [
    "http://normyartistry.com",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the route files
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(product_router, prefix="/products", tags=["products"])
app.include_router(order_router, prefix="/orders", tags=["orders"])
