import psycopg2
from src.config.env import DATABASE_CONFIG


class DatabaseHelper:
    def __init__(self):
        self.conn = psycopg2.connect(
            database=DATABASE_CONFIG.get("NAME"),
            host=DATABASE_CONFIG.get("HOST"),
            user=DATABASE_CONFIG.get("USER"),
            password=DATABASE_CONFIG.get("PASSWORD"),
            port=DATABASE_CONFIG.get("PORT"),
        )
