import redis
redis_db = redis.Redis(host="0.0.0.0")
redis_db.set('key', 'val')
print("testing", redis_db.get('key'))
