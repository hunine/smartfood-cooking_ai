import os
from dotenv import load_dotenv

load_dotenv()

REDIS = {
    "HOST": os.getenv("REDIS_HOST"),
    "PORT": os.getenv("REDIS_PORT"),
    "USERNAME": os.getenv("REDIS_USERNAME"),
    "PASSWORD": os.getenv("REDIS_PASSWORD"),
}
