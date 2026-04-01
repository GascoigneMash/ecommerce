from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Order, CartItem
from schemas import OrderCreate

router = APIRouter()

@router.post("/order")
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    # 1. Create the order
    new_order = Order(total=order_data.total)
    db.add(new_order)
    
    # 2. Clear the cart (Simplified logic)
    db.query(CartItem).delete()
    
    db.commit()
    db.refresh(new_order)
    return {"message": "Order placed successfully", "order_id": new_order.id}