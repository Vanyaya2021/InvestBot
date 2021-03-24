from telegram.ext import CommandHandler
from Configurations.config import CHOOSE_OFFICE_SECTION
from Keyboards.OfficeKeyboards import sectionsMarkup
from StaticMessages import welcome_office_message

def officeCommandHandler()-> CommandHandler:
    handler = CommandHandler(
        command= "my_office",
        callback= myOffice)
    return handler


def myOffice(bot, update) -> int:
    bot.message.reply_text(welcome_office_message, reply_markup=sectionsMarkup())
    return CHOOSE_OFFICE_SECTION