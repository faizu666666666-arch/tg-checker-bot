import os
from telethon.sync import TelegramClient

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
string_session = os.environ.get('STRING_SESSION')

client = TelegramClient(string_session, api_id, api_hash)

async def main():
    me = await client.get_me()
    print(f"Bot logged in as: {me.first_name}")

with client:
    client.loop.run_until_complete(main())
    with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
    import os
from telethon.sync import TelegramClient

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
string_session = os.environ.get('STRING_SESSION')

client = TelegramClient(string_session, api_id, api_hash)

async def main():
    me = await client.get_me()
    print(f"Bot logged in as: {me.first_name}")

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected() # This keeps the bot alive!
    
    
  
