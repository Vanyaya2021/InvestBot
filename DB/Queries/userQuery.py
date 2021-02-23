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

