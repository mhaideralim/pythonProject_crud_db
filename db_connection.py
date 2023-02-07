import asyncio
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

from beanie import Document, Indexed, init_beanie
from pymongo import MongoClient

client = AsyncIOMotorClient("mongodb://localhost:27017/")
try:
    client.admin.command('ismaster')
    print("Connected to the database successfully.")

except Exception as e:
    print(f"Could not connect to the database: {e}")

db = client["person_data"]
person_data = db["persons-data"]
