import telebot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Assalomu alaykum \n"+message.from_user.first_name)

if __name__ == '__main__':
    bot.polling(none_stop=True)
