from os import getenv
from dotenv import load_dotenv

load_dotenv()

TG_API_ID = getenv("TG_API_ID")
TG_API_HASH = getenv("TG_API_HASH")
TWITTER_API_ID = getenv("TWITTER_API_ID")
TWITTER_API_HASH = getenv("TWITTER_API_HASH")