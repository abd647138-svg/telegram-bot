import os
import telebot

TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "مرحبا بيك في البوت 🔥")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "وصلتني رسالتك: " + message.text)

print("البوت يخدم...")
bot.polling()
