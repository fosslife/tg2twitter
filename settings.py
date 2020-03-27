from os import getenv
from dotenv import load_dotenv

load_dotenv()

TG_API_ID = getenv("TG_API_ID")
TG_API_HASH = getenv("TG_API_HASH")

TWITTER_CLIENT_KEY = getenv("TWITTER_CLIENT_KEY")
TWITTER_CLIENT_SECRET = getenv("TWITTER_CLIENT_SECRET")

TWITTER_ACCESS_TOKEN = getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = getenv("TWITTER_ACCESS_TOKEN_SECRET")

channel_name=getenv("CHANNEL_NAME")