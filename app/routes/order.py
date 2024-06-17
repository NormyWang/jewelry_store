from fastapi import APIRouter, HTTPException
from app.data import orders, users, products
from app.models import Order
from datetime import datetime

router = APIRouter()

@router.post("/")
async def create_order(username: str, product_ids: list[int], quantities: list[int]):
    user = next((user for user in users if user.username == username), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if len(product_ids) != len(quantities):
        raise HTTPException(status_code=400, detail="Product IDs and quantities must match in length")
    
    order_id = len(orders) + 1
    order_date = datetime.now().isoformat()
    new_order = Order(order_id, user.username, product_ids, quantities, order_date)
    orders.append(new_order)
    return {"message": "Order created successfully", "order_id": order_id}
