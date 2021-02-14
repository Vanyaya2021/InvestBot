from telegram import (
    ReplyKeyboardRemove)
from telegram.ext import CommandHandler
from DB.Queries.userQuery import createUser


def startCommandHandler() -> CommandHandler:
    handler = CommandHandler(
        command="start",
        callback=startCommand)
    return handler


def helpCommandHandler() -> CommandHandler:
    handler = CommandHandler(
        command="help",
        callback=helpCommand)
    return handler


def menuCommandHandler() -> CommandHandler:
    handler = CommandHandler(
        command="menu",
        callback=menu)
    return handler


def helpCommand(bot,update):
    bot.message.reply_text("Я оперативно даю актуальную информацию о мире финансов."
                           "\nОзнакомиться с моими командами можешь ниже \n"
                           "\n/actualCurrency - Актуальные котировки"
                           "\n/companies - Компании на бирже"
                           "\n/news - Главные новости в мире финансов"
                           "\n/analytics - Аналитика и прогнозы"
                           "\n/teachMe - Обучу тебя основам финансовой грамотности"
                           "\n/myOffice - Твой личный кабинет"
                           "\n/menu - Переходи в меню"
                           "\n/help - Помогу разобраться тебе как я работаю"
                           "\n/start - Приветствие")


def startCommand(bot, update):
    res = createUser(bot)
    print(res)
    bot.message.reply_text(
        'Привет, я знаю много о финансах и могу поделиться актуальной информацией с тобой')
    bot.message.reply_text('Давай я познакомлю тебя с тем, что умею. Жми /help')


def menu(bot, update):
    bot.message.reply_text("Я оперативно даю актуальную информацию о мире финансов."
                           "\nОзнакомиться с моими командами можешь ниже \n"
                           "\n/actualCurrency - Актуальные котировки"
                           "\n/companies - Компании на бирже"
                           "\n/news - Главные новости в мире финансов"
                           "\n/analytics - Аналитика и прогнозы"
                           "\n/teachMe - Обучу тебя основам финансовой грамотности"
                           "\n/myOffice - Твой личный кабинет"
                           "\n/help - Помогу разобраться тебе как я работаю"
                           , reply_markup=ReplyKeyboardRemove())

