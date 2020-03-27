from os import getenv
from telethon import TelegramClient, events
import twitter
# import re
import settings

# Twitter

api = twitter.Api(consumer_key=settings.TWITTER_CLIENT_KEY, consumer_secret=settings.TWITTER_CLIENT_SECRET,
                  access_token_key=settings.TWITTER_ACCESS_TOKEN, access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)

# Telegram

with TelegramClient('name', settings.TG_API_ID, settings.TG_API_HASH) as client:
    @client.on(events.NewMessage(pattern=r"(.tweet)([ \S]+)", incoming=False, outgoing=True, chats=settings.channel_name))
    async def handler(event):
        tweet = event.pattern_match.group(2)
        await event.delete()
        try:
            api.PostUpdate(tweet)
            await event.respond(tweet)
        except:
            print("Could not post update")
            await event.respond(tweet)
    client.run_until_disconnected()
