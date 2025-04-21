from typing import Annotated
from fastapi import Depends, File, HTTPException, UploadFile


def get_image_file(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are allowed")

    return file


ImageAnnotatedDep = Annotated[UploadFile, Depends(get_image_file)]
