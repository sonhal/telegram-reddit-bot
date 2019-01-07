from connectors import telegram_connector

COMMANDS = ("top10", "top")


if __name__ == '__main__':
    tb = telegram_connector.TelegramBot()
    tb.start()
