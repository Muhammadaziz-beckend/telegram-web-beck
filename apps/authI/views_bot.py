import telebot
from django.conf import settings
import requests

TOKEN = settings.BOT_TOKEN
bot = telebot.TeleBot(TOKEN)

API_URL = "https://telegram-bot-apps.onrender.com/api/receive_phone/"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def send_web_app(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = telebot.types.KeyboardButton("📞 Поделиться номером", request_contact=True)
    keyboard.add(button)

    bot.send_message(message.chat.id, "Открывайте Mini App или отправьте номер телефона:", reply_markup=keyboard)

@bot.message_handler(content_types=["contact"])
def receive_contact(message):
    if message.contact:
        phone_number = message.contact.phone_number
        user_id = message.chat.id

        # Отправляем номер на бекенд
        response = requests.post(API_URL, json={"user_id": user_id, "phone": phone_number})

        bot.send_message(message.chat.id, f"Ваш номер {phone_number} получен!")

bot.polling()
