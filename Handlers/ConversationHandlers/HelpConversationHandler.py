from telegram.ext import ConversationHandler, CallbackQueryHandler
from Handlers.CommandHandlers.BaseCommandHandler import helpCommandHandler, startCommandHandler
from Configurations.config import ABOUT_COMMANDS,ABOUT_KEYBOARD, TO_MENU
from StaticMessages import help_about_commands_message,help_about_keyboard_message, menu_message
from Keyboards.Inline.WelcomeKeyboard import getSecondStepOfHelp, getThirdStepOfHelp
from Keyboards.General import menuMarkup



def helpConversationHandler() -> ConversationHandler:
    handler = ConversationHandler(
        entry_points=[helpCommandHandler()],
        states={
            ABOUT_COMMANDS: [CallbackQueryHandler(aboutCommands,pattern='send_info_about_commands')],
            ABOUT_KEYBOARD: [CallbackQueryHandler(aboutKeyboard, pattern='send_info_about_keyboards')],
            TO_MENU: [CallbackQueryHandler(bringToMenu, pattern='bring_to_menu')],
        },
        fallbacks=[startCommandHandler()] #нужно будет дописать все возможные выходы из разговора (команды котировок и т.д.)
    )
    return handler

def aboutCommands(bot, update) -> int:
    chatId = bot.callback_query.message.chat.id
    print(chatId)
    img = open("Static/WelcomePictures/aboutCommands.jpg",'rb')
    update.bot.sendPhoto(chatId,img,help_about_commands_message, reply_markup=getSecondStepOfHelp(), parse_mode="Markdown")
    return ABOUT_KEYBOARD

def aboutKeyboard(bot, update):
    chatId = bot.callback_query.message.chat.id
    img = open("Static/WelcomePictures/aboutKeyboard.jpg", 'rb')
    update.bot.sendPhoto(chatId, img, help_about_keyboard_message, reply_markup=getThirdStepOfHelp())
    return TO_MENU

def bringToMenu(bot, update):
    chatId = bot.callback_query.message.chat.id
    update.bot.sendMessage(chatId, menu_message, reply_markup=menuMarkup())
    return ConversationHandler.END