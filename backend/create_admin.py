from database import SessionLocal, Base, engine
from models import User
from security import get_password_hash

# 1. Make sure tables exist
Base.metadata.create_all(bind=engine)

# 2. Connect to DB
db = SessionLocal()

# 3. Create the Admin User
admin = User(
    username="gascoigne",
    hashed_password=get_password_hash("admin123"), # Password is 'admin123'
    role_level=0 # Level 3 = Root Admin
)

# 4. Add and Save
db.add(admin)
db.commit()

print("✅ Root Admin Created successfully!")
print("Username: gascoigne")
print("Password: admin123")