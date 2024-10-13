import tweepy
import os
import asyncio
from discord import Client

# Load Twitter API credentials from environment variables
api_key = os.getenv("TWITTER_API_KEY")
api_key_secret = os.getenv("TWITTER_API_KEY_SECRET")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

discord_client: Client = None

# Set Discord client globally (can be improved for better dependency injection)
def set_discord_client(client: Client):
    global discord_client
    discord_client = client

# Search terms for the Twitter bot to monitor
search_terms = ['python']

# Custom Tweepy streaming class
class MyStream(tweepy.StreamingClient):
    def __init__(self, bearer_token, message):
        super().__init__(bearer_token)
        self.message = message

    def on_connect(self):
        print("Connected to Twitter stream")

    async def send_tweet(self, tweet):
        # Sends tweet to the specified Discord channel
        try:
            await self.message.channel.send(tweet)
        except Exception as e:
            print(f"Error sending tweet to Discord: {e}")

    async def on_tweet(self, tweet):
        # Check if it's a standalone tweet (not a reply or retweet)
        if tweet.referenced_tweets is None and hasattr(self, "message"):
            tweet_text = tweet.data.get("text", "")
            await self.send_tweet(tweet_text)

# Fetches and sends the latest tweets of a specified user
async def fetch_tweets(message, username: str, limit: int = 5):
    try:
        # Get the latest tweets
        tweets = api.user_timeline(screen_name=username, count=limit, tweet_mode="extended", include_rts=False, exclude_replies=True)
        await message.channel.send(f"Top {limit} Tweets by {username}")
        
        for idx, tweet in enumerate(tweets[:limit], start=1):
            new_tweet = tweet.full_text.replace("\n", " ")
            await message.channel.send(f'{idx}. {tweet.user.screen_name} said: {new_tweet}')
            await message.channel.send(f"Link to tweet: https://twitter.com/twitter/status/{tweet.id}")

    except tweepy.TweepError as e:
        await message.channel.send(f"Error fetching tweets: {e}")
