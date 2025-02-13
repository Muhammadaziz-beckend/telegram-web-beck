import telebot
from django.conf import settings


TOKEN = settings.BOT_TOKEN
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button = telebot.types.KeyboardButton("Открыть Mini App", web_app=telebot.types.WebAppInfo(url="https://telegram-web-bot-i0ok.onrender.com/"))
    keyboard.add(button)
    bot.send_message(message.chat.id, "Открывайте Mini App", reply_markup=keyboard)

bot.polling()
