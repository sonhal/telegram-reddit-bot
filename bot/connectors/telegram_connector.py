from telegram.ext import Updater
from bot import utils
from telegram.ext import CommandHandler
from . import reddit_connector
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def add_start_handler(dispatcher):
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)


def reddit_handler(bot, update):
    message = ""
    for sub in reddit_connector.get_subreddit_hot("python", 10):
        message += "\n\n" + sub.title
    bot.send_message(chat_id=update.message.chat_id, text=message)
    logger = logging.getLogger()
    logger.info(f"Handling reddit call message({message})")



def add_reddit_handler(dispatcher):
    start_handler = CommandHandler('top10', reddit_handler)
    dispatcher.add_handler(start_handler)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


class TelegramBot:

    def __init__(self):
        env = utils.read_env()
        self.updater = Updater(token=env["TELEGRAM_TOKEN"])
        self.dispatcher = self.updater.dispatcher
        add_start_handler(dispatcher=self.dispatcher)
        add_reddit_handler(dispatcher=self.dispatcher)

    def start(self):
        self.updater.start_polling()
