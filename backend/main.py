from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import Base, engine
from backend.routes import products, cart, orders
from backend.routes import auth
from backend.routes import admin
from backend.security import get_password_hash, verify_password

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow your HTML file (frontend) to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, set this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router)
app.include_router(cart.router)
app.include_router(orders.router)
app.include_router(auth.router)
app.include_router(admin.router)

@app.get("/")
def read_root():
    return {"message": "Neon Precision API is Running"}