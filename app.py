#!/usr/bin/env python3

# Remember to:
# 1. pip install -r requirements.txt to install redis pacckage
# 2. Make sure redis-server is running and configured correctly on your OS
# 3. Import Redis package
import redis

# Setup Redis variables using your redis credentials
redis_host = "localhost"
redis_port = 6379
redis_password = ""


def redis_hello_world():
    """A very simple redis application - hello world! """

    # step 3: create the Redis Connection
    try:
        # Connect to the redis server
        r = redis.StrictRedis(host=redis_host, port=redis_port,
                              password=redis_password, decode_responses=True)

        # Create/set a redis message
        r.set("message", "Hello World from Redis!!")

        # Get the message from redis
        message = r.get("msg:hello")
        print(message)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    redis_hello_world()
