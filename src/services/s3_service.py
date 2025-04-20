import aioboto3
from fastapi import HTTPException
from typing import BinaryIO

from src.env import (
    S3_ACCESS_KEY_ID,
    S3_BUCKET_NAME,
    S3_HOST,
    S3_PORT,
    S3_SECRET_ACCESS_KEY,
)
from src.logger import logger


class S3Service:
    def __init__(self):
        self.session = aioboto3.Session()
        self.endpoint_url = f"http://{S3_HOST}:{S3_PORT}"
        self.aws_access_key_id = S3_ACCESS_KEY_ID
        self.aws_secret_access_key = S3_SECRET_ACCESS_KEY
        self.bucket_name = S3_BUCKET_NAME

    async def get_presigned_url(self, object_name: str) -> str:
        logger.info("Getting presigned url")
        async with self.session.client(
            "s3",
            endpoint_url=self.endpoint_url,
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
        ) as client:
            logger.info("Generating presigned url")
            return await client.generate_presigned_url(
                "get_object",
                Params={"Bucket": self.bucket_name, "Key": object_name},
                ExpiresIn=3600,
            )

    async def upload_file(
        self, object_name: str, file_data: BinaryIO, content_type: str
    ) -> str:
        logger.info("Uploading file")
        try:
            async with self.session.client(
                "s3",
                endpoint_url=self.endpoint_url,
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key,
            ) as client:
                await client.upload_fileobj(
                    file_data,
                    self.bucket_name,
                    object_name,
                    ExtraArgs={"ContentType": content_type},
                )
                logger.info("File uploaded")
            return object_name
        except Exception as err:
            logger.error(f"Error uploading file: {err}")
            raise HTTPException(status_code=500, detail=f"Error uploading file: {err}")


def get_s3_service() -> S3Service:
    return S3Service()
