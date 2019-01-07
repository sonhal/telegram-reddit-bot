import praw
from bot import utils


def get_get_configured_connection():
    env = utils.read_env()
    return praw.Reddit(client_id=env["CLIENT_ID"],  client_secret=env["CLIENT_SECRET"], user_agent=env["USER_AGENT"])


def get_subreddit_hot(subreddit, amount):
    if amount > 100: raise ValueError(f"amount({amount}) is over limit(100)")

    reddit_con = get_get_configured_connection()

    # assume you have a Reddit instance bound to variable `reddit`
    sub_r = reddit_con.subreddit(subreddit)

    hot = sub_r.hot(limit=amount)
    return hot
