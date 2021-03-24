from DB.Queries.companyQuerries import getSectors
from telegram import KeyboardButton,ReplyKeyboardMarkup



def commandMarkup():
    mosExchButton = KeyboardButton("Российский рынок")
    spbExchButton = KeyboardButton("Международный рынок")
    backButton = [KeyboardButton("     В меню    ")]
    buttons = [[mosExchButton, spbExchButton], backButton]
    markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True,resize_keyboard=True)
    return markup


def sectorMarkup(type):
    getSectorLst = getSectors(type)
    buttons = []
    for i in range(len(getSectorLst)):
        sectorButton = KeyboardButton(f'{getSectorLst[i]}')
        spam = []
        spam.append(sectorButton)
        buttons.append(spam)
    markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True,resize_keyboard=True)
    return markup

#print(sectorMarkup())




