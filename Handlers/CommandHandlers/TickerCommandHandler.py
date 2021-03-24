from telegram.ext import CommandHandler
from Configurations.config import CURRENCY
from Keyboards.OfficeKeyboards import sectionsMarkup
from StaticMessages import welcome_office_message

def tickerCommandHandler()-> CommandHandler:
    handler = CommandHandler(
        command = ['SBER','SBERP','GMKN','GAZP','FIVEDR','SNGS','SNGSP','YNDX','MOEX','ALRS'],
        callback= tickerInfo)
    return handler


def tickerInfo(bot, update) -> int:
    bot.message.reply_text("Здесь могла бы быть информация о бумаге")