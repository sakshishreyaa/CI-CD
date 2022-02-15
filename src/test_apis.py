import asyncio
from pydoc import cli
import redis
import os
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
MONGODB_URL = os.getenv("MONGODB_URL")
print("url", MONGODB_URL)
redis_db = redis.Redis(host="0.0.0.0")
redis_db.set('key', 'val')
print("testing", redis_db.get('key'))


client = AsyncIOMotorClient(str(MONGODB_URL))
print("mongi", client)
db = client.addressable_schedules


async def do_insert():
    document = {'key': 'value'}
    result = await db.meta_data.insert_one(document)
    print('insert', 'result %s' % repr(result.inserted_id))


async def do_find_one():
    document = await db.meta_data.find_one({'i': {'$lt': 2}})
    print('find', document)


loop = asyncio.get_event_loop()
loop.run_until_complete(do_insert())
loop = asyncio.get_event_loop()
loop.run_until_complete(do_find_one())
