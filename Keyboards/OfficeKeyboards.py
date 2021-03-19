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
        #inline_btn_1 = InlineKeyboardButton(text='Назад', callback_data='back_asset')
        inline_btn_1 = InlineKeyboardButton(text='Далее', callback_data='next_asset')
        #inline_btn_3 = InlineKeyboardButton(text ='График', callback_data='assets_graph')
        keyboard = InlineKeyboardMarkup([[inline_btn_1]])
        return keyboard