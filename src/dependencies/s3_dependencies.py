from typing import Annotated
from fastapi import Depends

from src.services.s3_service import S3Service


def get_s3_service() -> S3Service:
    return S3Service()


S3ServiceDep = Annotated[S3Service, Depends(get_s3_service)]
