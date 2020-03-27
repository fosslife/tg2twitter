from os import getenv
from telethon import TelegramClient, events

from config import TG_API_ID, TG_API_HASH

with TelegramClient('name', TG_API_ID, TG_API_HASH) as client:
    @client.on(events.NewMessage(pattern='.tweet'))
    async def handler(event):
        print("Got pattern")
        await event.reply('Hey!')

    client.run_until_disconnected()
