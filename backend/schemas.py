from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float
    description: str
    image: str
    category: str

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True

class CartItemBase(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    total: float