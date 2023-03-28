import os
from pathlib import Path
from pymongo import MongoClient
from dotenv import load_dotenv

# Load .env
dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

DATABASE = str(os.getenv('DATABASE'))
DB_URL = str(os.getenv('DB_URL'))

# Mongodb Connection
mongodb_client = MongoClient("mongodb://localhost:27017/")

# Select database
db = mongodb_client["testing"]
