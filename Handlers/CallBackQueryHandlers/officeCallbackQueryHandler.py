from telegram.ext import CallbackQueryHandler
from Configurations.config import CHOOSEN_MY_ASSETS

def nextAssetCallbackQueryHandler() -> CallbackQueryHandler:
    handler = CallbackQueryHandler(
        pattern='next_asset',
        callback=nextAsset)
    return handler

def nextAsset(bot, update) -> int:
    chatId = bot.callback_query.message.chat.id
    messageId = bot.callback_query.message.message_id
    print(bot.callback_query)
    message =""
    update.bot.editMessageText(message,chatId,messageId,"Markdown",)
    return CHOOSEN_MY_ASSETS

def backAssetCallbackQueryHandler() -> CallbackQueryHandler:
    handler = CallbackQueryHandler(
        pattern='back_asset',
        callback=backAsset)
    return handler

def backAsset(bot, update) -> int:
    chatId = bot.callback_query.message.chat.id
    messageId = bot.callback_query.message.message_id
    print(bot.callback_query)
    message =""
    update.bot.editMessageText(message,chatId,messageId,"Markdown",)
    return CHOOSEN_MY_ASSETS