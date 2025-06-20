from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.routes.analytics import router as analytics_router

app = FastAPI(
    title="Twitch Analytics API",
    version="1.0.0"
)

app.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])

def format_error(message: str):
    return {"error": message}


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=format_error(str(exc.detail))
    )