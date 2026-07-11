import os
from telethon import TelegramClient
from telethon.sessions import StringSession

# Load variables
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
string_session = os.environ.get('STRING_SESSION')

# Use StringSession to avoid file system errors
client = TelegramClient(StringSession(string_session), api_id, api_hash)

async def main():
    me = await client.get_me()
    print(f"Bot successfully logged in as: {me.first_name}")

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
        client.run_until_disconnected()
        
