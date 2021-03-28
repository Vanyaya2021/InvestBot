from telegram.ext import CallbackQueryHandler
from DB.Queries.userQuery import getUserFavoriteAssets
from Keyboards.General import FavoriteAssetsPaginationKeyboard
from Utility.assetCalculation import assetsMessage,generalMessageAboutUsersAssets
from Configurations.config import CHOOSEN_FAVORITE_ASSETS

def nextPageOfFavoriteAssetsCallbackQueryHandler() -> CallbackQueryHandler:
    handler = CallbackQueryHandler(
        pattern="^nextPageFA_[+-]?(0|[1-9][0-9]*)$",
        callback=nextPage)
    return handler

def nextPage(bot, update) -> int:
    chatId = bot.callback_query.message.chat.id
    messageId = bot.callback_query.message.message_id
    callbackData = bot.callback_query.data
    page = int(callbackData.split('_')[1])
    userAssets,allPages = getUserFavoriteAssets(chatId, page)
    elementsOnPage = len(userAssets)
    message = assetsMessage(userAssets)
    update.bot.editMessageText(message, chatId, messageId, parse_mode = "Markdown", reply_markup = FavoriteAssetsPaginationKeyboard(page, elementsOnPage, allPages))
    return CHOOSEN_FAVORITE_ASSETS

def backPageOfFavoriteAssetsCallbackQueryHandler() -> CallbackQueryHandler:
    handler = CallbackQueryHandler(
        pattern="^backPageFA_[+-]?(0|[1-9][0-9]*)$",
        callback=backPage)
    return handler

def backPage(bot, update) -> int:
    chatId = bot.callback_query.message.chat.id
    messageId = bot.callback_query.message.message_id
    callbackData = bot.callback_query.data
    page = int(callbackData.split('_')[1])
    userAssets,allPages = getUserFavoriteAssets(chatId, page)
    elementsOnPage = len(userAssets)
    message = assetsMessage(userAssets)
    update.bot.editMessageText(message, chatId, messageId, parse_mode="Markdown",
                               reply_markup=FavoriteAssetsPaginationKeyboard(page, elementsOnPage, allPages))
    return CHOOSEN_FAVORITE_ASSETS