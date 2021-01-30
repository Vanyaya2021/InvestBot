from telegram.ext import Updater
from Configurations import config
from Handlers.CommandHandlers.BaseCommandHandler import startCommandHandler, helpCommandHandler, menuCommandHandler
from Handlers.ConversationHandlers.CurrencyConversationHandler import currencyConversationHandler


def main() -> None:
    my_bot = Updater(config.token, config.url, use_context=True)

    my_bot.dispatcher.add_handler(startCommandHandler())
    my_bot.dispatcher.add_handler(helpCommandHandler())

    my_bot.dispatcher.add_handler(currencyConversationHandler())

    my_bot.start_polling()  # проверяет о наличии сообщений с платформы Telegram
    my_bot.idle()  # бот будет работать пока его не остановят


if __name__ == "__main__":
    main()
