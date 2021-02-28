from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters
from Configurations.config import CURRENCY
from Handlers.CommandHandlers.BaseCommandHandler import menuCommandHandler
from Handlers.CommandHandlers.CurrencyCommandHandler import currency
from Keyboards.CurrencyKeybord import toolsMarkup, stocksMarkup


def currencyConversationHandler()-> ConversationHandler:
    handler = ConversationHandler(
        entry_points=[CommandHandler('actualCurrency', currency),
                      MessageHandler(Filters.regex('^(Актуальные котировки)$'), currency)],
        states={
            CURRENCY: [MessageHandler(Filters.regex('^(Российский рынок|российские|Российские)$'), mosCurrency),
                       MessageHandler(Filters.regex('^(Международный рынок|международные)$'), spbCurrency),
                       MessageHandler(Filters.regex('^(Акции|акции)$'), stocks),
                       MessageHandler(Filters.regex('^(Назад|назад)$'), back),
                       ],
        },
        fallbacks=[menuCommandHandler()]
    )
    return handler


def mosCurrency(bot, update)-> int:
    tools(bot)
    return CURRENCY

def back(bot, update)-> int:
    print("back")
    currency(bot, update)
    return CURRENCY


def spbCurrency(bot, update)-> int:
    tools(bot)
    return CURRENCY


def tools(bot)-> int:
    bot.message.reply_text("Какие финансовые инструменты интересуют?"
                           , reply_markup=toolsMarkup())
    return CURRENCY


def stocks(bot, update)-> int:
    bot.message.reply_text("Самые популярные:\n"
                           "\nЯндекс(YNDX) стоит тыщутыщ.\n"
                           "Изменение за сегодня 500%\n"
                           "\nСбербанк(SBER) стоит 40 гривен.\n"
                           "Изменение за сегодня -3%"
                           , reply_markup=stocksMarkup())
    return CURRENCY

