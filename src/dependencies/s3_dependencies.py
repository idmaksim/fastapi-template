from typing import Annotated
from fastapi import Depends

from src.services.s3_service import S3Service, get_s3_service


S3ServiceAnnotatedDep = Annotated[S3Service, Depends(get_s3_service)]
