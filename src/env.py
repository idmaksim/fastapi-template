import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
REFRESH_TOKEN_SECRET = os.getenv("REFRESH_TOKEN_SECRET")
CACHE_TTL = int(os.getenv("CACHE_TTL"))

envs = [
    DATABASE_URL,
    ACCESS_TOKEN_SECRET,
    REFRESH_TOKEN_SECRET,
    CACHE_TTL,
]


def check_env():
    for env in envs:
        if env is None:
            raise ValueError(f"Environment variable {env} is not set")
