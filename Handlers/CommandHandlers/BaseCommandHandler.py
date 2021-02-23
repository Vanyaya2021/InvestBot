from telegram import (
    ReplyKeyboardRemove)
from telegram.ext import CommandHandler
from DB.Queries.userQuery import createUser
from StaticMessages import menu_message, welcome_message
from Configurations.config import ABOUT_COMMANDS

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
    bot.message.reply_text(menu_message)
    return ABOUT_COMMANDS


def startCommand(bot, update):
    res = createUser(bot)
    print(res)
    bot.message.reply_text(
        "Привет, я знаю много о финансах и могу поделиться актуальной информацией с тобой. Пройди обучение как со мной работать"
        "по команде /help или сразу переходи в интересующий раздел")
    bot.message.reply_text(menu_message)


def menu(bot, update):
    bot.message.reply_text(welcome_message+menu_message, reply_markup=ReplyKeyboardRemove())

