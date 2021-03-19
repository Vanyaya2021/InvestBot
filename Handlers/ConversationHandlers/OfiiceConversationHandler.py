from telegram.ext import ConversationHandler, MessageHandler, Filters
from Handlers.CommandHandlers.OfficeCommandHandler import officeCommandHandler
from Handlers.CommandHandlers.BaseCommandHandler import menuCommandHandler
from DB.Queries.userQuery import getUserAssets
from Utility.assetCalculation import assetsMessage
from Keyboards.OfficeKeyboards import infoAboutAssetsKeyboard
from Handlers.CallBackQueryHandlers.officeCallbackQueryHandler import nextAssetCallbackQueryHandler,backAssetCallbackQueryHandler
from Configurations.config import CHOOSE_OFFICE_SECTION,CHOOSEN_MY_ASSETS

def officeConversationHandler() -> ConversationHandler:
    handler = ConversationHandler(
        entry_points=[officeCommandHandler()],
        states={
            CHOOSE_OFFICE_SECTION: [MessageHandler(Filters.regex('^(Мой портфель 💳)$'), myAssets),
                                    MessageHandler(Filters.regex('^(Избранное ⭐)$'), myFavorites),
                                    MessageHandler(Filters.regex('^(Настройка пуш-уведомлений 🛎)$'), myPushNotifications),
                                    MessageHandler(Filters.regex('^(В меню)$'), toMenu),],
            CHOOSEN_MY_ASSETS:[nextAssetCallbackQueryHandler(),
                               backAssetCallbackQueryHandler()],
        },
        fallbacks=[] #нужно будет дописать все возможные выходы из разговора (команды котировок и т.д.)
    )
    return handler

def myAssets(bot,update) -> int:
    chat_id = bot.message.chat.id
    userAssets = getUserAssets(chat_id)
    message = assetsMessage(userAssets)
    bot.message.reply_text(message, parse_mode = "Markdown", reply_markup = infoAboutAssetsKeyboard(userAssets))
    return CHOOSEN_MY_ASSETS

def myFavorites(bot,update):
    return None

def myPushNotifications(bot,update):
    return None

def toMenu(bot,update):
    menuCommandHandler()
    return ConversationHandler.END

