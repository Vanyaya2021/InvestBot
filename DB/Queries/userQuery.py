from DB.Queries import dbConnection as db
from DB.Models.User import User
import uuid, datetime



def createUser(bot):
    user = User
    user.id = uuid.uuid4()
    user.chat_id = bot.message.chat.id
    user.username = bot.message.chat.username
    user.first_name = bot.message.chat.first_name
    user.last_name = bot.message.chat.last_name
    user.join_date = datetime.datetime.now(tz = datetime.timezone.utc)
    result = db.query("INSERT INTO botdb.public.user_t (id, chat_id, username, first_name, last_name, join_date)"
              "VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(user.id, user.chat_id, user.username,user.first_name,
                                                                     user.last_name,user.join_date))
    return result

def getUserByChatId(userChatId):
    result = db.query("SELECT * FROM botdb.public.user_t WHERE chat_id ={}".format(userChatId))
    user = User
    user.id = result[0][0]
    user.chat_id = result[0][1]
    user.username = result[0][2]
    user.first_name = result[0][3]
    user.last_name = result[0][4]
    user.join_date = result[0][5]
    return user

def getUserAssets(userChatId, page):
    pageSize = 4
    user = getUserByChatId(userChatId)
    result = db.query("SELECT user_id,ticker_id,name,description,ticker_type,"
                      "ticker_amount,book_value,actual_price,last_trading_day_price, "
                      "is_favorite from botdb.public.user_assets_t a "
                      "JOIN botdb.public.ticker_t b  "
                      "ON a.ticker_id = b.id WHERE user_id ='{0}' order by name asc".format(user.id))
    list = result[(page-1)*pageSize:page*pageSize]
    if page == 0:
        return result #возвращает все активы пользователя
    return list







