from telegram.ext import CallbackQueryHandler, ConversationHandler
from StaticMessages import help_about_commands_message,help_about_keyboard_message, menu_message
from Keyboards.Inline.WelcomeKeyboard import getSecondStepOfHelp, getThirdStepOfHelp
from Keyboards.General import menuMarkup
from Configurations.config import ABOUT_COMMANDS,ABOUT_KEYBOARD, TO_MENU

def firstNextButtonCallbackQueryHandler() -> CallbackQueryHandler:
    handler = CallbackQueryHandler(
        pattern='send_info_about_commands',
        callback=aboutCommands)
    return handler

def aboutCommands(bot, update) -> int:
    chatId = bot.callback_query.message.chat.id
    print(chatId)
    img = open("Static/WelcomePictures/aboutCommands.jpg",'rb')
    update.bot.sendPhoto(chatId,img,help_about_commands_message, reply_markup=getSecondStepOfHelp(), parse_mode="Markdown")
    return ABOUT_KEYBOARD

def secondNextButtonCallbackQueryHandler() -> CallbackQueryHandler:
    handler = CallbackQueryHandler(
        pattern='send_info_about_keyboards',
        callback=aboutKeyboard)
    return handler

def aboutKeyboard(bot, update) -> int:
    chatId = bot.callback_query.message.chat.id
    img = open("Static/WelcomePictures/aboutKeyboard.jpg", 'rb')
    update.bot.sendPhoto(chatId, img, help_about_keyboard_message, reply_markup=getThirdStepOfHelp())
    return TO_MENU

def toMenuButtonCallbackQueryHandler() -> CallbackQueryHandler:
    handler = CallbackQueryHandler(
        pattern='bring_to_menu',
        callback=bringToMenu)
    return handler

def bringToMenu(bot, update):
    chatId = bot.callback_query.message.chat.id
    update.bot.sendMessage(chatId, menu_message, reply_markup=menuMarkup())
    return ConversationHandler.END