from telegram import KeyboardButton, ReplyKeyboardMarkup
from DB.Queries.companyQuerries import getSectors


def sectorMarkup():
    getSectorLst = getSectors()
    buttons = []
    for i in range(len(getSectorLst)):
        sectorButton = KeyboardButton(f'{getSectorLst[i]}')
        spam = []
        spam.append(sectorButton)
        buttons.append(spam)
    markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True,resize_keyboard=True)
    return markup

#print(sectorMarkup())

