from telegram.ext import CommandHandler
from Configurations.config import CURRENCY
from Keyboards.CurrencyKeabord import commandMarkup


def currencyCommandHandler()-> CommandHandler:
    handler = CommandHandler(
        command= "actualCurrency",
        callback= currency)
    return handler


def currency(bot, update) -> int:
    bot.message.reply_text("Введи тикер или название бумаги,"
                           "значение которой хотел бы посмотреть."
                           "Если не знаешь, что искать,"
                           "смотри самые популярные бумаги на рынках."
                           , reply_markup=commandMarkup())
    return CURRENCY


