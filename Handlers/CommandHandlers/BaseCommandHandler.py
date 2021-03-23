from telegram import (
    ReplyKeyboardRemove)
from telegram.ext import CommandHandler
from DB.Queries.userQuery import createUser
from StaticMessages import menu_message, welcome_message, start_message, start_help_message
from Configurations.config import ABOUT_COMMANDS
from Keyboards.General import menuMarkup
from Keyboards.Inline.WelcomeKeyboard import getFirstStepOfHelp

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


def helpCommand(bot,update) -> int:
    bot.message.reply_text(start_help_message, reply_markup = getFirstStepOfHelp())
    return ABOUT_COMMANDS


def startCommand(bot, update):
    res = createUser(bot)
    bot.message.reply_text(start_message,reply_markup = menuMarkup())


def menu(bot, update):
    bot.message.reply_text(welcome_message+menu_message, reply_markup=ReplyKeyboardRemove())

