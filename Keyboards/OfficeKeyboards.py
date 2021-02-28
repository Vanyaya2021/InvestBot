from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def sectionsMarkup():
    button1 = KeyboardButton("Мой портфель 💳")
    button2 = KeyboardButton("Избранное ⭐️")
    button3 = [KeyboardButton("Настройка пуш-уведомлений 🛎")]
    button4 = [KeyboardButton("В меню")]
    buttons = [[button1, button2], button3,button4]
    markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True, resize_keyboard=True)
    return markup

def infoAboutAssetsKeyboard():
    inline_btn_1 = InlineKeyboardButton(text ='Активы', callback_data='assets')
    keyboard = InlineKeyboardMarkup([[inline_btn_1]])
    return keyboard