from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Product as ProductModel  # Renamed to ProductModel to avoid confusion
from ..schemas import Product, ProductBase    # Make sure we import BOTH schemas
from ..security import require_role

router = APIRouter()

@router.get("/products", response_model=list[Product])
def get_products(db: Session = Depends(get_db)):
    # Use ProductModel to query the database
    products = db.query(ProductModel).all()
    return products

@router.post("/products", dependencies=[Depends(require_role(1))])
def create_product(product: ProductBase, db: Session = Depends(get_db)):
    db_product = ProductModel(**product.model_dump()) 
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Only Staff (Level 1) or Higher can DELETE products
@router.delete("/products/{product_id}", dependencies=[Depends(require_role(1))])
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted"}