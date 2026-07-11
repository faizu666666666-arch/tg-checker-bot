import os
import asyncio
from telethon.sync import TelegramClient

# Get variables from Railway
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
string_session = os.environ.get('STRING_SESSION')

# Setup client
client = TelegramClient(string_session, api_id, api_hash)

async def main():
    # Verify login
    me = await client.get_me()
    print(f"Bot logged in as: {me.first_name}")

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
        client.run_until_disconnected()
        
