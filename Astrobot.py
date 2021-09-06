import telebot
import datetime
# from telebot import types
bot = telebot.TeleBot("1879281515:AAEyNmgzQREkGsxR2oI8CW1twXiGCrbWPYA")

@bot.message_handler(commands=['promos'])
def promote(message):
    id = message.text.split()
    bot.promote_chat_member(message.chat.id,id[1],can_change_info=True,can_delete_messages=True,can_invite_users=True,can_restrict_members=True,can_pin_messages=True,can_promote_members=True)

@bot.message_handler(commands=['my_id'])
def send_id(message):
    bot.send_message(message.chat.id,"Your id: "+str(message.from_user.id))

@bot.message_handler(commands=['start'])
def starts(message):
    bot.send_message(message.chat.id,"Hey there, Check the channel @Astronomydeck")

bot.polling()
