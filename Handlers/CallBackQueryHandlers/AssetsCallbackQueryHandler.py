from telegram.ext import CallbackQueryHandler
from DB.Queries.userQuery import getUserAssets
from Keyboards.General import AssetsPaginationKeyboard,menuMarkup
from Utility.assetCalculation import assetsMessage,generalMessageAboutUsersAssets
from Configurations.config import CHOOSEN_MY_ASSETS

def nextPageOfAssetsCallbackQueryHandler() -> CallbackQueryHandler:
    handler = CallbackQueryHandler(
        pattern="^nextPageA_[+-]?(0|[1-9][0-9]*)$",
        callback=nextPage)
    return handler

def nextPage(bot, update) -> int:
    chatId = bot.callback_query.message.chat.id
    messageId = bot.callback_query.message.message_id
    callbackData = bot.callback_query.data
    page = int(callbackData.split('_')[1])
    userAssets,allPages = getUserAssets(chatId, page)
    elementsOnPage = len(userAssets)
    generalMessage = generalMessageAboutUsersAssets(chatId)
    message = assetsMessage(userAssets)
    update.bot.editMessageText(generalMessage + message, chatId, messageId, parse_mode = "Markdown", reply_markup = AssetsPaginationKeyboard(page, elementsOnPage, allPages))
    return CHOOSEN_MY_ASSETS

def backPageOfAssetsCallbackQueryHandler() -> CallbackQueryHandler:
    handler = CallbackQueryHandler(
        pattern="^backPageA_[+-]?(0|[1-9][0-9]*)$",
        callback=backPage)
    return handler

def backPage(bot, update) -> int:
    chatId = bot.callback_query.message.chat.id
    messageId = bot.callback_query.message.message_id
    callbackData = bot.callback_query.data
    page = int(callbackData.split('_')[1])
    userAssets,allPages = getUserAssets(chatId, page)
    elementsOnPage = len(userAssets)
    generalMessage = generalMessageAboutUsersAssets(chatId)
    message = assetsMessage(userAssets)
    update.bot.editMessageText(generalMessage + message, chatId, messageId, parse_mode="Markdown",
                               reply_markup=AssetsPaginationKeyboard(page, elementsOnPage, allPages))
    return CHOOSEN_MY_ASSETS