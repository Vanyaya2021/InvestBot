from telegram.ext import ConversationHandler, MessageHandler, Filters
from Handlers.CommandHandlers.OfficeCommandHandler import officeCommandHandler
from Handlers.CommandHandlers.BaseCommandHandler import menu
from Handlers.CommandHandlers.TickerCommandHandler import tickerCommandHandler
from Handlers.CallBackQueryHandlers.paginationCallbackQueryHandler import nextPageCallbackQueryHandler,backPageCallbackQueryHandler
from Keyboards.OfficeKeyboards import sectionsMarkup
from Keyboards.General import paginationKeyboard
from Keyboards.Inline.PushNotificationsKeyboards import getPushNotificationKeyboard
from Handlers.CallBackQueryHandlers.pushNotificationManager import pushPriceCallbackQueryHandler,pushNewsCallbackQueryHandler
from StaticMessages import welcome_office_message,push_static_message
from Utility.assetCalculation import assetsMessage,generalMessageAboutUsersAssets
from DB.Queries.userQuery import getUserAssets,getUserByChatId
from Configurations.config import CHOOSE_OFFICE_SECTION,CHOOSEN_MY_ASSETS,MANAGE_PUSH

def officeConversationHandler() -> ConversationHandler:
    handler = ConversationHandler(
        entry_points=[officeCommandHandler(),MessageHandler(Filters.regex('^(Личный кабинет)$'), myOffice)],
        states={
            CHOOSE_OFFICE_SECTION: [MessageHandler(Filters.regex('^(Мой портфель 💳)$'), myAssets),
                                    MessageHandler(Filters.regex('^(Избранное️ 🌟)$'), myAssetsFav),
                                    MessageHandler(Filters.regex('^(Настройка пуш-уведомлений 🛎)$'), myPushNotifications),
                                    MessageHandler(Filters.regex('^(В меню)$'), toMenu)],
            CHOOSEN_MY_ASSETS:[nextPageCallbackQueryHandler(),
                               backPageCallbackQueryHandler(),
                               MessageHandler(Filters.regex('^(В меню)$'), toMenu)],
            MANAGE_PUSH:[pushPriceCallbackQueryHandler(),pushNewsCallbackQueryHandler()]
        },
        fallbacks=[tickerCommandHandler()] #нужно будет дописать все возможные выходы из разговора (команды котировок и т.д.)
    )
    return handler

def myOffice(bot, update) -> int:
    bot.message.reply_text(welcome_office_message, reply_markup=sectionsMarkup())
    return CHOOSE_OFFICE_SECTION

def myAssets(bot,update) -> int:
    chatId = bot.message.chat.id
    userAssets,allPages = getUserAssets(chatId, page = 1)
    elementsOnPage = len(userAssets)
    generalMessage = generalMessageAboutUsersAssets(chatId)
    message = assetsMessage(userAssets)
    bot.message.reply_text(generalMessage+message, parse_mode = "Markdown",
                           reply_markup = paginationKeyboard(page=1,elements_on_page=elementsOnPage,all_pages=allPages))
    return CHOOSEN_MY_ASSETS

def myPushNotifications(bot,update) -> int:
    chatId = bot.message.chat.id
    user = getUserByChatId(chatId)
    signPrice = "вкл. ✅" if user.push_price_change == True else "выкл. ❌"
    signNews = "вкл. ✅" if user.push_news_about_company == True else "выкл. ❌"
    bot.message.reply_text(push_static_message.format(signPrice, signNews),
                           reply_markup=getPushNotificationKeyboard(user.push_price_change,user.push_news_about_company))
    return MANAGE_PUSH

def myAssetsFav(bot,update) -> int:
    bot.message.reply_text("kfmvkldfmvoldfkmv")
    return ConversationHandler.END

def toMenu(bot,update) -> int:
    menu(bot, update)
    return ConversationHandler.END

