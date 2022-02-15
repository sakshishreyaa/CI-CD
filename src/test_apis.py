from pydoc import cli
import redis
import os
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
MONGODB_URL = os, os.getenv("MONGODB_URL")
redis_db = redis.Redis(host="0.0.0.0")
redis_db.set('key', 'val')
print("testing", redis_db.get('key'))


client = AsyncIOMotorClient(str(MONGODB_URL))
print("mongi", client)
