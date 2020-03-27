# Telegram 2 Twitter bot

## Description
This bot lets you send a text message to any of your telegram channel, and then it will be automatically posted to
your Twitter account as well. Only text is supported as of now. 

## Installation
```
git clone https://github.com/fosslife/tg2twitter.git
```

```
pipenv shell
pipenv install
```

make a file called `.env`. Get following keys from respective developer account
```
TG_API_ID=''
TG_API_HASH=''

TWITTER_CLIENT_KEY=''
TWITTER_CLIENT_SECRET=''

TWITTER_ACCESS_TOKEN=''
TWITTER_ACCESS_TOKEN_SECRET=''

CHANNEL_NAME=your_channel_name_or_id
```

Getting twitter API keys is a Huge mess. I followed [this](https://python-twitter.readthedocs.io/en/latest/getting_started.html) tutorial

Then run the bot
```
python3 main.py
```


## Usage

If bot runs successfully you need to sign in to your telegram account first. after that
just send a message with `.tweet` at the start. bot will automatically post that message
to your twitter
ex:
```
.tweet Hello Telegram and Twitter
```

PS: just send this to channel, the bot will automatically delete this entire message
immedietly, remove the `.tweet` part from message automatically and post the original
text in both places. 



## TODO
- Make stringsession for easy deployments
- character limit