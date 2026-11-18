import telebot

TOKEN = "حط_التوكن_هنا"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "اهلا بيك، البوت يخدم 🔥")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "وصلتني رسالتك: " + message.text)

print("البوت يخدم...")
bot.polling()
