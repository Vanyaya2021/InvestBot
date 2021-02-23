from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters
from Handlers.CommandHandlers.BaseCommandHandler import helpCommandHandler
from Configurations.config import ABOUT_COMMANDS,ABOUT_KEYBOARD

def helpConversationHandler()-> ConversationHandler:
    handler = ConversationHandler(
        entry_points=[helpCommandHandler()],
        states={
            ABOUT_COMMANDS: [
                       ],
        },
        fallbacks=[]
    )
    return handler