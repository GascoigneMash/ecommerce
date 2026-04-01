from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routes import products, cart, orders
from routes import auth
from routes import admin

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