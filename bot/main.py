from connectors import reddit_connector, telegram_connector

COMMANDS = ("top10", "top")


def handle_command(subreddit, command):
    if command in COMMANDS:
        return reddit_connector.get_subreddit_hot(subreddit, 10)




def main():
    res = handle_command("cars", "top10")
    for r in res:
        print(r.title)


if __name__ == '__main__':
    tb = telegram_connector.TelegramBot()
    tb.start()
