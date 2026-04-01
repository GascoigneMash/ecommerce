import sys
import os

# 1. Add the CURRENT folder to Python's search path
# This ensures Python can find 'backend' even if running from a different directory
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# 2. Import the app from main.py
# Because of the path insert above, this works even if main.py is in the same folder
from backend.main import app

# 3. Expose the app for Uvicorn
# This is what the deployment server calls
application = app