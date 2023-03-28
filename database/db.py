import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load .env
load_dotenv()

DATABASE: str = os.environ.get("DATABASE", "TestingDB")
DB_URL: str = os.environ.get("DB_URL")

# Mongodb Connection
mongodb_client = MongoClient((f"mongodb://{DB_URL}/"))


# Select database
database = mongodb_client[str(DATABASE)]
