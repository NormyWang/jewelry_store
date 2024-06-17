from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import List
from pydantic import BaseModel

# Import SQLAlchemy models and database setup from models.py
from app.models import User as DBUser, Product as DBProduct, Order as DBOrder, engine, Base
from app.routes.user import router as users_router
from app.routes.product import router as products_router
from app.routes.order import router as orders_router
f

# Import Pydantic models
from app.schemas import User, Product, Order

# Bind engine to metadata
Base.metadata.bind = engine

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

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


# Mount the users router
app.include_router(users_router, prefix="/users")
app.include_router(products_router, prefix="/products")
app.include_router(orders_router, prefix="/orders")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Example endpoints using Pydantic models
@app.post("/users/", response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    db_user = DBUser(username=user.username, password=user.password, email=user.email, address=user.address)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user  # Return Pydantic model

@app.post("/products/", response_model=Product)
def create_product(product: Product, db: Session = Depends(get_db)):
    db_product = DBProduct(name=product.name, description=product.description, price=product.price,
                         quantity=product.quantity, image_url=product.image_url)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return product  # Return Pydantic model

@app.post("/orders/", response_model=Order)
def create_order(order: Order, db: Session = Depends(get_db)):
    db_order = DBOrder(user_id=order.user_id, order_date=datetime.utcnow())
    for product in order.products:
        db_product = DBProduct(**product.dict())
        db.add(db_product)
        db_order.products.append(db_product)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return order  # Return Pydantic model

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user  # Return SQLAlchemy model

# Handle exceptions
@app.exception_handler(Exception)
async def exception_handler(request, exc):
    return JSONResponse(status_code=500, content={"message": "Internal server error"})

