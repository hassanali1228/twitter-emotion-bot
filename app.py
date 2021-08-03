import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):

    logger.info("Retrieving mentions")
    new_since_id = since_id

    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)

        if tweet.in_reply_to_status_id is None:
            continue

        tweet_id=tweet.in_reply_to_status_id

        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")
            stimulus=(api.get_status(id=tweet_id)).text

            response = f"I think they're just sad... 😢, when they said \"{stimulus}\""

            logger.info(response)

            api.update_status(
                status=response,
                in_reply_to_status_id=tweet.id,
            )

    return new_since_id

def main():

    api = create_api()
    since_id = 1
    
    while True:
        since_id = check_mentions(api, ["analyze"], since_id)
        logger.info("Waiting...")
        time.sleep(10)

if __name__ == "__main__":
    main()