from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Клавиатура для сообщения Help после команд
def getFirstStepOfHelp():
    inline_btn_1 = InlineKeyboardButton(text ='Далее', callback_data='send_info_about_commands')
    keyboard = InlineKeyboardMarkup([[inline_btn_1]])
    return keyboard

def getSecondStepOfHelp():
    inline_btn_1 = InlineKeyboardButton(text ='Далее', callback_data='send_info_about_keyboards')
    keyboard = InlineKeyboardMarkup([[inline_btn_1]])
    return keyboard

def getThirdStepOfHelp():
    inline_btn_1 = InlineKeyboardButton(text='В меню', callback_data='bring_to_menu')
    keyboard = InlineKeyboardMarkup([[inline_btn_1]])
    return keyboard