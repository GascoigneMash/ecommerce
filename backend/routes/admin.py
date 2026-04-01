from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User, Order
from security import require_role

router = APIRouter()

# LEVEL 2: Manager Only - View Revenue
@router.get("/admin/revenue", dependencies=[Depends(require_role(2))])
def get_revenue(db: Session = Depends(get_db)):
    # Calculate total revenue from all orders
    orders = db.query(Order).all()
    total_revenue = sum(order.total for order in orders)
    
    # In a real app, you'd group by day/week. Here is a summary.
    return {
        "total_revenue": total_revenue,
        "total_orders": len(orders),
        "average_order_value": total_revenue / len(orders) if orders else 0
    }

# LEVEL 3: Admin Only - User Management (Promote/Demote)
@router.get("/admin/users", dependencies=[Depends(require_role(3))])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    # Don't return passwords!
    return [{"id": u.id, "username": u.username, "role_level": u.role_level} for u in users]

@router.put("/admin/users/{user_id}/role", dependencies=[Depends(require_role(3))])
def update_user_role(user_id: int, new_role: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Prevent locking yourself out if you are the only admin? (Optional logic)
    
    user.role_level = new_role
    db.commit()
    return {"message": f"User {user.username} updated to Level {new_role}"}