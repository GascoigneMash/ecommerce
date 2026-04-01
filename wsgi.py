import sys
import os

# This forces Python to check the folder where this file lives first
sys.path.insert(0, os.getcwd())

from backend.main import app

application = app