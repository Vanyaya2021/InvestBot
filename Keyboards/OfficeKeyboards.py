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

def infoAboutAssetsKeyboard(userAssets):
    if len(userAssets)<=3:
        keyboard = InlineKeyboardMarkup([[]])
        return keyboard
    else:
        inline_btn_1 = InlineKeyboardButton(text='➡️ Стр. 2', callback_data='nextPage_2')
        keyboard = InlineKeyboardMarkup([[inline_btn_1]])
        return keyboard