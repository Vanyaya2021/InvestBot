from telegram.ext import CallbackQueryHandler
from telegram import ReplyKeyboardMarkup
from DB.Queries.userQuery import getUserAssets
from Keyboards.General import paginationKeyboard,menuMarkup
from Utility.assetCalculation import assetsMessage,generalMessageAboutUsersAssets
from Configurations.config import CHOOSEN_MY_ASSETS

def nextPageCallbackQueryHandler() -> CallbackQueryHandler:
    handler = CallbackQueryHandler(
        pattern="^nextPage_[+-]?(0|[1-9][0-9]*)$",
        callback=nextPage)
    return handler

def nextPage(bot, update) -> int:
    chatId = bot.callback_query.message.chat.id
    messageId = bot.callback_query.message.message_id
    callbackData = bot.callback_query.data
    page = int(callbackData.split('_')[1])
    userAssets = getUserAssets(chatId, page)
    generalMessage = generalMessageAboutUsersAssets(chatId)
    message = assetsMessage(userAssets)
    update.bot.editMessageText(generalMessage+message,chatId,messageId,parse_mode = "Markdown", reply_markup = paginationKeyboard(page,len(userAssets)))
    return CHOOSEN_MY_ASSETS

def backPageCallbackQueryHandler() -> CallbackQueryHandler:
    handler = CallbackQueryHandler(
        pattern="^backPage_[+-]?(0|[1-9][0-9]*)$",
        callback=backPage)
    return handler

def backPage(bot, update) -> int:
    chatId = bot.callback_query.message.chat.id
    messageId = bot.callback_query.message.message_id
    callbackData = bot.callback_query.data
    page = int(callbackData.split('_')[1])
    userAssets = getUserAssets(chatId, page)
    generalMessage = generalMessageAboutUsersAssets(chatId)
    message = assetsMessage(userAssets)
    update.bot.editMessageText(generalMessage + message, chatId, messageId, parse_mode="Markdown",
                               reply_markup=paginationKeyboard(page, len(userAssets)))
    return CHOOSEN_MY_ASSETS