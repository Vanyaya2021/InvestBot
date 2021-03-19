from telegram.ext import Updater
from Configurations import config
from Handlers.CommandHandlers.BaseCommandHandler import startCommandHandler, helpCommandHandler, menuCommandHandler
from Handlers.ConversationHandlers.CurrencyConversationHandler import currencyConversationHandler
from Handlers.ConversationHandlers.HelpConversationHandler import helpConversationHandler
from Handlers.ConversationHandlers.OfiiceConversationHandler import officeConversationHandler


def main() -> None:
    my_bot = Updater(config.token, use_context=True)

    my_bot.dispatcher.add_handler(startCommandHandler(),2)

    my_bot.dispatcher.add_handler(helpConversationHandler(),1)
    my_bot.dispatcher.add_handler(currencyConversationHandler(),1)
    my_bot.dispatcher.add_handler(officeConversationHandler(), 1)

    my_bot.start_polling()  # проверяет о наличии сообщений с платформы Telegram
    my_bot.idle()  # бот будет работать пока его не остановят


if __name__ == "__main__":
    main()
