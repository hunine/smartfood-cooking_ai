import os
from dotenv import load_dotenv

load_dotenv()

REDIS = {
    "HOST": os.getenv("REDIS_HOST"),
    "PORT": os.getenv("REDIS_PORT"),
    "USERNAME": os.getenv("REDIS_USERNAME"),
    "PASSWORD": os.getenv("REDIS_PASSWORD"),
}

DATABASE_CONFIG = {
    "NAME": os.getenv("DATABASE_NAME"),
    "HOST": os.getenv("DATABASE_HOST"),
    "USER": os.getenv("DATABASE_USER"),
    "PASSWORD": os.getenv("DATABASE_PASSWORD"),
    "PORT": os.getenv("DATABASE_PORT"),
}
