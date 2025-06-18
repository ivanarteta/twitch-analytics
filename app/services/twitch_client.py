import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")

TOKEN_URL = "https://id.twitch.tv/oauth2/token"
BASE_URL = "https://api.twitch.tv/helix"
ACCESS_TOKEN = None

async def get_token():
    return ACCESS_TOKEN

async def get_user_info():
    return None

async def get_live_streams():
    return None