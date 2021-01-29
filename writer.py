import redis

redis_handle = redis.Redis( host='<your_redis_host>', port=<your_redis_port>, password='<your_redis_password>')

numKey = "numKey"

redis_handle.delete(numKey)
redis_handle.rpush(numKey, *(range(1, 101, 1)))
numList = redis_handle.lrange(numKey, 0, -1)
print([x.decode("UTF-8") for x in numList])
