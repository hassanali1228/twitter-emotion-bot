import tweepy
import logging
import os

logger = logging.getLogger()

from dotenv import load_dotenv, dotenv_values
secrets = dotenv_values(".env")

def create_api():
    # consumer_key = os.getenv("CONSUMER_KEY")
    # consumer_secret = os.getenv("CONSUMER_SECRET")
    # access_token = os.getenv("ACCESS_TOKEN")
    # access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    [consumer_key, consumer_secret, access_token, access_token_secret] = [secrets["consumerKey"], secrets["consumerSecret"], 
                                                                            secrets["accessToken"], secrets["accessSecret"]]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api