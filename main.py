import telebot

TOKEN = "9127855024:AAHBANudjezUUO9ytD9wLq8YvlAoS_0uQng"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "اهلا بيك، البوت يخدم 🔥")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "وصلتني رسالتك: " + message.text)

print("البوت يخدم...")
bot.polling()
