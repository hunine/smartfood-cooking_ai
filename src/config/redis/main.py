import redis
from src.config.env import REDIS


class RedisConfig:
    def __init__(self):
        self.redis_config = redis.Redis(
            host=REDIS.get("HOST"),
            port=REDIS.get("PORT"),
            username=REDIS.get("USERNAME"),
            password=REDIS.get("PASSWORD"),
        )
