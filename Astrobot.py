import telebot
import datetime
# from telebot import types
bot = telebot.TeleBot("1879281515:AAEyNmgzQREkGsxR2oI8CW1twXiGCrbWPYA")

bot.send_message('@Darknessoft','Hello)   
bot.set_webhook(url="http://example.com", certificate=open('mycert.pem'))
bot.polling()
