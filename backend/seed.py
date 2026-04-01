from database import SessionLocal, engine, Base
from models import Product

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Check if data exists
if db.query(Product).count() == 0:
    products = [
        Product(name="AXION X1 PRO", price=1299.00, description="Liquid Retina XDR, A17 Bionic.", image="https://lh3.googleusercontent.com/aida-public/AB6AXuB-HgWp2MFDw4_FOelCXYUG-Xcdw4uIjVMjk8_3TA3h8sTG_sl0GlFI8TLZWPPe8advKrKbhRJkRMCxeLcLIqDQNTRspNUNsTdAGGXFakFTcW4eAeqdAvhd9eEK6HZzpFmh41zUm0uJLyDX94F0xASHy586r8zq8Fraq_grtoJHjQNBkktwZML4iTNiBf06_ape6LaFbbgzqFHr5BdQkk37g1OYgVLKzwg1befl57g9wwimCxFJXYJ-wnW6Jiitk2d9Lhf0ZHgD8UA", category="Smartphones"),
        Product(name="SONIC CORE V2", price=450.00, description="Active Spatial Audio, 60h Playback.", image="https://lh3.googleusercontent.com/aida-public/AB6AXuBgRNODE4AtCZUlfDMUPJs0QdEzUyq2oDC5zC3wrXqthO5vkWOmA7nAOK8bkFK8_ls761VaQn30OCNpblPX4HUD2Bnco4UTgj2vd0jnyUM49KiwaPKUDTNuTBcro7HgLQxBjosFv7Q7J3VkTKEEQ_FOutOUvlf0O5_BfhXrEJeuNf3sbRsO8EOlUfsXAIeBYBebOt_DSuWnra9ebQP9_5qQ94FkyR1YE91vuEo1r3xwCa0rTwL-GB3VC4YKP5Fqia_AFjaXBccRir0", category="Audio"),
        Product(name="CHRONOS ELITE", price=799.00, description="Titanium Housing, Sapphire Display.", image="https://lh3.googleusercontent.com/aida-public/AB6AXuDncAKvOC0O8mEYM1P-bMXj-JezXHnzVCCqpwqpqpBOmAc9tixgs5RusTl3Xn0PoUz95NCJHahz9tLRCKehZlN3TfF6CVAT0cw2wiER3BSPAaRhxw8nwEeBWw3Sw_-wgCw2yJYvZmt-3B-OZIrVWLk3qTCU-1vl6Ib87LAoAsPCHUSqSHZI_3iqBlB2npOEjnB30WJk5iGOlKpG3DQ0OVZCw7BEwOh5rVSoHWRdvsH713Nhf1gwBYXX5VNYcUh87yXd_A0uFJnXxx8", category="Wearables"),
    ]
    
    for p in products:
        db.add(p)
    
    db.commit()
    print("🌱 Database seeded successfully!")
else:
    print("Database already has data.")
    
db.close()