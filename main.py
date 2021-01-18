from telegram.ext import Updater
from telegram.ext import CommandHandler
from Configurations import config
from Handlers.CommandHandlers.startCommand import startCommand
from Handlers.CommandHandlers.helpCommand import helpCommand

def main():
    my_bot = Updater(config.token, config.url, use_context=True)

    my_bot.dispatcher.add_handler(CommandHandler('start', startCommand))  # обработчик команды '/start'
    my_bot.dispatcher.add_handler(CommandHandler('help', helpCommand))  # обработчик команды '/start'
    my_bot.start_polling()  # проверяет о наличии сообщений с платформы Telegram
    my_bot.idle()  # бот будет работать пока его не остановят

if __name__ == "__main__":
    main()