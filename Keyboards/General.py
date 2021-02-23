from telegram import KeyboardButton, ReplyKeyboardMarkup

def menuMarkup():
    Button1 = KeyboardButton("Актуальные котировки")
    Button2 = KeyboardButton("Компании на бирже")
    Button3 = KeyboardButton("Новости")
    Button4 = KeyboardButton("Аналитика и прогнозы")
    Button5 = KeyboardButton("Личный кабинет")
    Button6 = KeyboardButton("Основы финансовой грамотности")
    buttons = [[Button1, Button2], [Button3,Button4],[Button5,Button6]]
    markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True)
    return markup