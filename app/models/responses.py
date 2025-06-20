from fastapi import HTTPException
from fastapi.responses import JSONResponse


def raise_http_error(status_code: int, message: str):
    raise HTTPException(
        status_code=status_code,
        detail=message
    )
