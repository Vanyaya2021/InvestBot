from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from Configurations.config import pageSize

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

def AssetsPaginationKeyboard(page, elements_on_page, all_pages):
    if page == 1:
        if elements_on_page<pageSize:
            keyboard = InlineKeyboardMarkup([[]])
        else:
            inline_btn_1 = InlineKeyboardButton(text='➡️ Стр. {0}'.format(page + 1), callback_data='nextPageA_{}'.format(page + 1))
            keyboard = InlineKeyboardMarkup([[inline_btn_1]])
    elif page == all_pages:
        inline_btn_1 = InlineKeyboardButton(text='Стр. {0} ⬅️'.format(page - 1),
                                            callback_data='backPageA_{}'.format(page - 1))
        keyboard = InlineKeyboardMarkup([[inline_btn_1]])
    else:
        inline_btn_1 = InlineKeyboardButton(text='Стр. {0} ⬅️'.format(page - 1), callback_data='backPageA_{}'.format(page - 1))
        inline_btn_2 = InlineKeyboardButton(text='➡️ Стр. {0}'.format(page + 1), callback_data='nextPageA_{}'.format(page + 1))
        keyboard = InlineKeyboardMarkup([[inline_btn_1,inline_btn_2]])
    return keyboard

def FavoriteAssetsPaginationKeyboard(page, elements_on_page, all_pages):
    if page == 1:
        if elements_on_page<pageSize:
            keyboard = InlineKeyboardMarkup([[]])
        else:
            inline_btn_1 = InlineKeyboardButton(text='➡️ Стр. {0}'.format(page + 1), callback_data='nextPageFA_{}'.format(page + 1))
            keyboard = InlineKeyboardMarkup([[inline_btn_1]])
    elif page == all_pages:
        inline_btn_1 = InlineKeyboardButton(text='Стр. {0} ⬅️'.format(page - 1),
                                            callback_data='backPageFA_{}'.format(page - 1))
        keyboard = InlineKeyboardMarkup([[inline_btn_1]])
    else:
        inline_btn_1 = InlineKeyboardButton(text='Стр. {0} ⬅️'.format(page - 1), callback_data='backPageFA_{}'.format(page - 1))
        inline_btn_2 = InlineKeyboardButton(text='➡️ Стр. {0}'.format(page + 1), callback_data='nextPageFA_{}'.format(page + 1))
        keyboard = InlineKeyboardMarkup([[inline_btn_1,inline_btn_2]])
    return keyboard