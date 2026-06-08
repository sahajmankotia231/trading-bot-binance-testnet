from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

def get_client():

    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    if not api_key or not api_secret:
        raise ValueError(
            "API_KEY or API_SECRET missing in .env"
        )

    return Client(
        api_key,
        api_secret,
        testnet=True
    )