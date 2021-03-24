from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

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

def paginationKeyboard(currentPage,elementsOnPage):
    if currentPage == 1:
        inline_btn_1 = InlineKeyboardButton(text='➡️ Стр. {0}'.format(currentPage+1), callback_data='nextPage_{}'.format(currentPage+1))
        keyboard = InlineKeyboardMarkup([[inline_btn_1]])
    elif elementsOnPage<4:
        inline_btn_1 = InlineKeyboardButton(text='Стр. {0} ⬅️'.format(currentPage - 1),
                                            callback_data='backPage_{}'.format(currentPage - 1))
        keyboard = InlineKeyboardMarkup([[inline_btn_1]])
    else:
        inline_btn_1 = InlineKeyboardButton(text='Стр. {0} ⬅️'.format(currentPage-1), callback_data='backPage_{}'.format(currentPage-1))
        inline_btn_2 = InlineKeyboardButton(text='➡️ Стр. {0}'.format(currentPage+1), callback_data='nextPage_{}'.format(currentPage+1))
        keyboard = InlineKeyboardMarkup([[inline_btn_1,inline_btn_2]])
    return keyboard