from fastapi import FastAPI
from app.routes.analytics import router as analytics_router

app = FastAPI(
    title="Twitch Analytics API",
    version="1.0.0"
)

app.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])
