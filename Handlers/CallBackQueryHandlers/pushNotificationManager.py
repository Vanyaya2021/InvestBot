from telegram.ext import CallbackQueryHandler
from DB.Queries.userQuery import getUserByChatId,updatePushPrice,updatePushNews
from StaticMessages import push_static_message
from Keyboards.Inline.PushNotificationsKeyboards import getPushNotificationKeyboard
from Utility.assetCalculation import assetsMessage,generalMessageAboutUsersAssets
from Configurations.config import MANAGE_PUSH


def pushPriceCallbackQueryHandler() -> CallbackQueryHandler:
    handler = CallbackQueryHandler(
        pattern="pushPrice",
        callback=pushPrice)
    return handler

def pushPrice(bot, update) -> int:
    chatId = bot.callback_query.message.chat.id
    messageId = bot.callback_query.message.message_id
    user = getUserByChatId(chatId)
    buttonText = bot.callback_query.message.reply_markup.inline_keyboard[0][0].text
    push_price_change = False if buttonText.find('Вкл') == -1 else True
    user = getUserByChatId(chatId)
    signPrice = "вкл. ✅" if push_price_change == True else "выкл. ❌"
    signNews = "вкл. ✅" if user.push_news_about_company == True else "выкл. ❌"
    update.bot.editMessageText(push_static_message.format(signPrice, signNews),chatId,messageId,
                           reply_markup=getPushNotificationKeyboard(push_price_change,user.push_news_about_company))

    updatePushPrice(user.id, push_price_change)
    return MANAGE_PUSH

def pushNewsCallbackQueryHandler() -> CallbackQueryHandler:
    handler = CallbackQueryHandler(
        pattern="pushNews",
        callback=pushNews)
    return handler

def pushNews(bot, update) -> int:
    chatId = bot.callback_query.message.chat.id
    messageId = bot.callback_query.message.message_id
    user = getUserByChatId(chatId)
    buttonText = bot.callback_query.message.reply_markup.inline_keyboard[1][0].text
    push_news_about_company = False if buttonText.find('Вкл') == -1 else True
    user = getUserByChatId(chatId)

    signPrice = "вкл. ✅" if user.push_price_change == True else "выкл. ❌"
    signNews = "вкл. ✅" if push_news_about_company == True else "выкл. ❌"

    update.bot.editMessageText(push_static_message.format(signPrice, signNews),chatId,messageId,
                           reply_markup=getPushNotificationKeyboard(user.push_price_change,push_news_about_company))

    updatePushNews(user.id, push_news_about_company)
    return MANAGE_PUSH
