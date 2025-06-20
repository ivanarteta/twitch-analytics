import os
from dotenv import load_dotenv
import httpx
from fastapi import HTTPException

load_dotenv()

CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")

TOKEN_URL = "https://id.twitch.tv/oauth2/token"
BASE_URL = "https://api.twitch.tv/helix"
ACCESS_TOKEN = None

async def get_token():
    global ACCESS_TOKEN
    if ACCESS_TOKEN:
        return ACCESS_TOKEN
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            TOKEN_URL,
            params={
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "grant_type": "client_credentials"
            }
        )

    if response.status_code != 200:
        raise HTTPException(status_code=401, detail="Twitch could not retreive token")

    ACCESS_TOKEN = response.json().get("access_token")
    return ACCESS_TOKEN   

async def get_user_info(id):
    token = await get_token()
    print(token)
    return None

async def get_live_streams():
    return None