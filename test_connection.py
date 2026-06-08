from bot.client import get_client

try:
    client = get_client()
    print("Connected Successfully")

except Exception as error:
    print(f"Connection Failed: {error}")