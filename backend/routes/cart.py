from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import CartItem, User
from schemas import CartItemBase
from security import require_role, get_current_user

router = APIRouter()

# Helper: Get cart items specific to the logged-in user
def get_user_cart(db: Session, user_id: int):
    return db.query(CartItem).filter(CartItem.user_id == user_id).all()

@router.post("/cart/add", dependencies=[Depends(require_role(0))])
def add_to_cart(item: CartItemBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Check if item exists for THIS specific user
    existing = db.query(CartItem).filter(
        CartItem.product_id == item.product_id,
        CartItem.user_id == current_user.id
    ).first()
    
    if existing:
        existing.quantity += item.quantity
    else:
        # Create new item with user_id attached
        db_item = CartItem(
            product_id=item.product_id, 
            quantity=item.quantity,
            user_id=current_user.id # CRITICAL: Tie to user
        )
        db.add(db_item)
    
    db.commit()
    return {"message": "Item added to cart"}

@router.get("/cart", dependencies=[Depends(require_role(0))])
def get_cart(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Return only the current user's cart
    return get_user_cart(db, current_user.id)

@router.delete("/cart/{item_id}", dependencies=[Depends(require_role(0))])
def delete_cart_item(item_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Ensure user can only delete their OWN items
    item = db.query(CartItem).filter(CartItem.id == item_id).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Security Check: Does this item belong to the user?
    if item.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Access Denied: Not your item")
        
    db.delete(item)
    db.commit()
    return {"message": "Item removed"}