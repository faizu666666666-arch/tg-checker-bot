import os
from telethon import TelegramClient, events, functions, types
from telethon.sessions import StringSession

# Load variables
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
string_session = os.environ.get('STRING_SESSION')

# Setup client
client = TelegramClient(StringSession(string_session), api_id, api_hash)

# Handler: Ping
@client.on(events.NewMessage(pattern='/ping'))
async def ping_handler(event):
    await event.respond('I am alive!')

# Handler: Check Number
@client.on(events.NewMessage(pattern='/check (.+)'))
async def check_number(event):
    phone = event.pattern_match.group(1).strip()
    contact = types.InputPhoneContact(client_id=0, phone=phone, first_name="Check", last_name="")
    
    try:
        result = await client(functions.contacts.ImportContactsRequest([contact]))
        if result.users:
            await event.respond(f"✅ {phone} is ON Telegram.")
        else:
            await event.respond(f"❌ {phone} is NOT on Telegram.")
    except Exception as e:
        await event.respond(f"⚠️ Error: Could not check {phone}.")

async def main():
    me = await client.get_me()
    print(f"Bot successfully logged in as: {me.first_name}")

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
        client.run_until_disconnected()
        
