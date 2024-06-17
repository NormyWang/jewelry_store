from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from datetime import datetime

# SQLAlchemy base
Base = declarative_base()

# Association table for order products
order_products = Table('order_products', Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.order_id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)

# User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    address = Column(String)

    # Relationship to orders
    orders = relationship("Order", back_populates="user")

# Product model
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)
    image_url = Column(String)

    # Relationship to orders
    orders = relationship("Order", secondary=order_products, back_populates="products")

# Order model
class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    order_date = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="orders")
    products = relationship("Product", secondary=order_products, back_populates="orders")
