# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

# Import route files
from app.routes import main_router

# Import database and models
from app.database import engine, Base
from app.models.user_model import UserModel
from app.models.order_model import OrderModel, OrderProductModel
from app.models.product_model import ProductModel

# FastAPI app
app = FastAPI()

# Static file serving
# Adjust this path as needed to point to your static directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# CORS configuration
origins = [
    "http://normyartistry.com",
    "http://localhost:8080",
    "http://localhost:8081"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Mount the route files
app.include_router(main_router)

@app.on_event("startup")
async def startup_event():
    # You can add any startup logic here if needed
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # You can add any cleanup logic here if needed
    pass

# Test route for serving an image
@app.get("/test-image")
async def test_image():
    image_path = os.path.join(static_dir, "image", "products", "e1.jpeg")
    if os.path.exists(image_path):
        return FileResponse(image_path)
    else:
        return {"error": "Image not found"}

# Optional: Add a root route for API health check
@app.get("/")
async def root():
    return {"message": "Welcome to the Jewelry Store API"}