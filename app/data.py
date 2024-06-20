from app.models.user_model import User as DBUser
from app.models.product_model import Product as DBProduct
from app.models.order_model import Order as DBOrder

users = []
products = []
orders = []

# Adding some sample products for demonstration purposes
products.append(Product(1, "Necklace", "Gold necklace", 150.00, 10, "static/image/products/n1.jpeg"))
products.append(Product(2, "Necklace", "necklace", 180.00, 10, "static/image/products/n2.jpeg"))
products.append(Product(3, "Necklace", "silber necklace", 100.00, 18, "static/image/products/n3.jpeg"))
products.append(Product(4, "Necklace", "Gold necklace", 120.00, 19, "static/image/products/n4.jpeg"))
products.append(Product(5, "Ring", "Silber ring", 200.00, 5, "static/image/products/r1.jpeg"))
products.append(Product(6, "Ring", "Diamond ring", 2010.00, 9, "static/image/products/r2.jpeg"))
products.append(Product(7, "Ring", "Diamond ring", 2900.00, 5, "static/image/products/r3.jpeg"))
products.append(Product(8, "Ring", "Silber ring", 400.00, 5, "static/image/products/r4.jpeg"))
products.append(Product(9, "Earrings", "Pearl earrings", 80.00, 20, "static/image/products/e1.jpeg"))
products.append(Product(10, "Earrings", "Pearl earrings", 70.00, 20, "static/image/products/e2.jpeg"))
products.append(Product(11, "Earrings", "Pearl earrings", 60.00, 20, "static/image/products/e3.jpeg"))
products.append(Product(12, "Earrings", "Pearl earrings", 50.00, 20, "static/image/products/e4.jpeg"))