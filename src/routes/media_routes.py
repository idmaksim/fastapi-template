from fastapi import APIRouter

from src.dependencies.jwt_dependencies import JwtDep
from src.dependencies.file_dependencies import ImageAnnotatedDep
from src.dependencies.s3_dependencies import S3ServiceAnnotatedDep
from src.env import CACHE_TTL
from fastapi_cache.decorator import cache

router = APIRouter(prefix="/media", tags=["media"], dependencies=[JwtDep])


@router.post("/upload")
async def upload_media(
    file: ImageAnnotatedDep,
    s3_service: S3ServiceAnnotatedDep,
):
    return await s3_service.upload_file(file.filename, file.file, file.content_type)


@router.get("/presigned-url/{object_name}")
@cache(expire=CACHE_TTL)
async def get_presigned_url(
    s3_service: S3ServiceAnnotatedDep,
    object_name: str,
):
    return await s3_service.get_presigned_url(object_name)
