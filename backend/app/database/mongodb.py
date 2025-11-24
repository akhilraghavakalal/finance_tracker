from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional

class MongoDB:
    client: Optional[AsyncIOMotorClient] = None
    
mongodb = MongoDB()

async def connect_to_mongo():
    """Connect to MongoDB"""
    mongodb.client = AsyncIOMotorClient("mongodb://localhost:27017")
    print("✅ Connected to MongoDB!")

async def close_mongo_connection():
    """Close MongoDB connection"""
    mongodb.client.close()
    print("❌ Closed MongoDB connection")

def get_database():
    """Get database instance"""
    return mongodb.client.finance_tracker