import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
REFRESH_TOKEN_SECRET = os.getenv("REFRESH_TOKEN_SECRET")

CACHE_TTL = int(os.getenv("CACHE_TTL"))

S3_HOST = os.getenv("S3_HOST")
S3_PORT = os.getenv("S3_PORT")
S3_ACCESS_KEY_ID = os.getenv("S3_ACCESS_KEY_ID")
S3_SECRET_ACCESS_KEY = os.getenv("S3_SECRET_ACCESS_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

envs = [
    DATABASE_URL,
    ACCESS_TOKEN_SECRET,
    REFRESH_TOKEN_SECRET,
    CACHE_TTL,
    S3_HOST,
    S3_PORT,
    S3_ACCESS_KEY_ID,
    S3_SECRET_ACCESS_KEY,
    S3_BUCKET_NAME,
]


def check_env():
    for env in envs:
        if env is None:
            raise ValueError(f"Environment variable {env} is not set")
