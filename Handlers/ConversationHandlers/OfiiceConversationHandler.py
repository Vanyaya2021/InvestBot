from telegram.ext import ConversationHandler, MessageHandler, Filters
from Handlers.CommandHandlers.OfficeCommandHandler import officeCommandHandler
from Handlers.CommandHandlers.BaseCommandHandler import menuCommandHandler
from DB.Queries.userQuery import getUserAssets
from Utility.assetCalculation import assetsMessage,generalMessageAboutUsersAssets
from Keyboards.OfficeKeyboards import infoAboutAssetsKeyboard,sectionsMarkup
from Handlers.CallBackQueryHandlers.paginationCallbackQueryHandler import nextPageCallbackQueryHandler,backPageCallbackQueryHandler
from StaticMessages import welcome_office_message
from Configurations.config import CHOOSE_OFFICE_SECTION,CHOOSEN_MY_ASSETS

def officeConversationHandler() -> ConversationHandler:
    handler = ConversationHandler(
        entry_points=[officeCommandHandler(),MessageHandler(Filters.regex('^(Личный кабинет)$'), myOffice)],
        states={
            CHOOSE_OFFICE_SECTION: [MessageHandler(Filters.regex('^(Мой портфель 💳)$'), myAssets),
                                    MessageHandler(Filters.regex('^(Избранное ⭐)$'), myFavorites),
                                    MessageHandler(Filters.regex('^(Настройка пуш-уведомлений 🛎)$'), myPushNotifications),
                                    MessageHandler(Filters.regex('^(В меню)$'), toMenu),],
            CHOOSEN_MY_ASSETS:[nextPageCallbackQueryHandler(),backPageCallbackQueryHandler()]
        },
        fallbacks=[] #нужно будет дописать все возможные выходы из разговора (команды котировок и т.д.)
    )
    return handler

def myOffice(bot, update) -> int:
    bot.message.reply_text(welcome_office_message, reply_markup=sectionsMarkup())
    return CHOOSE_OFFICE_SECTION

def myAssets(bot,update) -> int:
    chatId = bot.message.chat.id
    userAssets = getUserAssets(chatId,page = 1)
    generalMessage = generalMessageAboutUsersAssets(chatId)
    message = assetsMessage(userAssets)
    bot.message.reply_text(generalMessage+message, parse_mode = "Markdown", reply_markup = infoAboutAssetsKeyboard(userAssets))
    return CHOOSEN_MY_ASSETS

def myFavorites(bot,update):
    return None

def myPushNotifications(bot,update):
    return None

def toMenu(bot,update):
    menuCommandHandler()
    return ConversationHandler.END

