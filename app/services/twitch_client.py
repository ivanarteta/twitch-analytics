import os
from dotenv import load_dotenv
import httpx
from fastapi import HTTPException
from app.models.responses import raise_http_error

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

    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": CLIENT_ID
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/users", params={"id": id}, headers=headers)

    if response.status_code == 401:
        raise_http_error(401, "Unauthorized. Twitch access token is invalid or has expired.")
    elif response.status_code == 404:
        raise_http_error(404, "User not found")
    elif response.status_code == 500:
        raise_http_error(500, "Internal server error")  

    return response.json().get("data", [])[0]

async def get_live_streams():
    token = await get_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": CLIENT_ID
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/streams", headers=headers)

    if response.status_code == 401:
        raise_http_error(401, "Unauthorized. Twitch access token is invalid or has expired.")
    elif response.status_code == 500:
        raise_http_error(500, "Internal server error")  

    streams = response.json().get("data", [])
    return [{"title": stream["title"], "user_name": stream["user_name"]} for stream in streams]