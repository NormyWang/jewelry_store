# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import route files
from app.routes import main_router

# FastAPI app
app = FastAPI()

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

# Mount the route files
app.include_router(main_router)