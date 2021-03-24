from telegram.ext import ConversationHandler, MessageHandler, Filters
from Handlers.CommandHandlers.BaseCommandHandler import helpCommandHandler
from Configurations.config import ABOUT_COMMANDS,ABOUT_KEYBOARD, TO_MENU
from Handlers.CallBackQueryHandlers.helpCallbackQueryHandler import firstNextButtonCallbackQueryHandler,secondNextButtonCallbackQueryHandler,toMenuButtonCallbackQueryHandler



def helpConversationHandler() -> ConversationHandler:
    handler = ConversationHandler(
        entry_points=[helpCommandHandler()],
        states={
            ABOUT_COMMANDS: [firstNextButtonCallbackQueryHandler()],
            ABOUT_KEYBOARD: [secondNextButtonCallbackQueryHandler()],
            TO_MENU: [toMenuButtonCallbackQueryHandler()],
        },
        fallbacks=[MessageHandler(Filters.regex('^(Актуальные котировки|Компании на бирже|Новости|Аналитика и прогнозы|Личный кабинет|Основы финансовой грамотности)$'),ConversationHandler.END)] #нужно будет дописать все возможные выходы из разговора (команды котировок и т.д.)
    )
    return handler

