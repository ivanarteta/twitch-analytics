from fastapi import APIRouter, HTTPException, Query
from app.services.twitch_client import get_user_info, get_live_streams

router = APIRouter()


@router.get("/user")
async def get_user(id: str = Query(..., description="Twitch user ID")):
    if not id or not id.strip():
        raise HTTPException(status_code=400, detail="Invalid or missing 'id' parameter.")
    return await get_user_info(id)


@router.get("/streams")
async def get_streams():
    return await get_live_streams()
