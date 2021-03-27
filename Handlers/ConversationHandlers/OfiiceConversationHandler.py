from telegram.ext import ConversationHandler, MessageHandler, Filters
from Handlers.CommandHandlers.OfficeCommandHandler import officeCommandHandler
from Handlers.CommandHandlers.BaseCommandHandler import menu
from Handlers.CommandHandlers.TickerCommandHandler import tickerCommandHandler
from DB.Queries.userQuery import getUserAssets
from Utility.assetCalculation import assetsMessage,generalMessageAboutUsersAssets
from Keyboards.OfficeKeyboards import sectionsMarkup
from Handlers.CallBackQueryHandlers.paginationCallbackQueryHandler import nextPageCallbackQueryHandler,backPageCallbackQueryHandler
from StaticMessages import welcome_office_message
from Keyboards.General import paginationKeyboard
from Configurations.config import CHOOSE_OFFICE_SECTION,CHOOSEN_MY_ASSETS

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
                               MessageHandler(Filters.regex('^(В меню)$'), toMenu)]
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
    bot.message.reply_text("Заглушка1")
    return ConversationHandler.END

def myAssetsFav(bot,update) -> int:
    bot.message.reply_text("Заглушка2")
    return ConversationHandler.END

def toMenu(bot,update) -> int:
    menu(bot, update)
    return ConversationHandler.END

