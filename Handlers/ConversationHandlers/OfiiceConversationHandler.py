from telegram.ext import ConversationHandler, MessageHandler, Filters
from Handlers.CommandHandlers.OfficeCommandHandler import officeCommandHandler
from Configurations.config import CHOOSE_OFFICE_SECTION

def officeConversationHandler() -> ConversationHandler:
    handler = ConversationHandler(
        entry_points=[officeCommandHandler()],
        states={
            CHOOSE_OFFICE_SECTION: [],
        },
        fallbacks=[] #нужно будет дописать все возможные выходы из разговора (команды котировок и т.д.)
    )
    return handler