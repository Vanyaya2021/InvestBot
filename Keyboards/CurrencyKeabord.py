from telegram import KeyboardButton, ReplyKeyboardMarkup


def commandMarkup():
    mosExchButton = KeyboardButton("Российский рынок")
    spbExchButton = KeyboardButton("Международный рынок")
    backButton = [KeyboardButton("     В меню    ")]
    buttons = [[mosExchButton, spbExchButton], backButton]
    markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True,resize_keyboard=True)
    return markup


def toolsMarkup():
    aButton = KeyboardButton("     Акции     ")
    vButton = KeyboardButton("     Валюты    ")
    iButton = KeyboardButton("     Индексы    ")
    fButton = KeyboardButton("     Фьючерсы    ")
    backButton = [KeyboardButton("Назад в актуальные котировки")]
    buttons = [[aButton, vButton], [iButton, fButton], backButton]
    markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True,resize_keyboard=True)
    return markup


def stocksMarkup():
    aButton = KeyboardButton("       YNDX      ")
    vButton = KeyboardButton("       SBER      ")
    backButton = [KeyboardButton("Назад")]
    buttons = [[aButton, vButton], backButton]
    markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True,resize_keyboard=True)
    return markup
