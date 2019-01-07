import praw
from bot.reddit import config
from bot import utils


def get_get_configured_connection():
    env = utils.read_env()
    return praw.Reddit(client_id=env["CLIENT_ID"],  client_secret=env["CLIENT_SECRET"], user_agent=config.user_agent)
