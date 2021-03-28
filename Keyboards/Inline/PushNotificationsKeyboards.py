from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Клавиатура для сообщения Help после команд
def getPushNotificationKeyboard(is_push_price_available,is_push_news_available ):
    textButton1 = "Включить пуши по цене +-5% ✅" if is_push_price_available == False else "Выключить пуши по цене +-5% ❌"
    textButton2 = "Включить пуши по новостям ✅" if is_push_news_available == False else "Выключить пуши по новостям ❌"
    inline_btn_1 = InlineKeyboardButton(text =textButton1, callback_data='pushPrice')
    inline_btn_2 = InlineKeyboardButton(text=textButton2, callback_data='pushNews')
    keyboard = InlineKeyboardMarkup([[inline_btn_1],[inline_btn_2]])
    return keyboard