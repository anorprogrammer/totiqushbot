import telebot

bot = telebot.TeleBot('1718923163:AAGVqnCBqWKUjTPMTFtSqyA7K_2v1vhTm3c')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Assalomu alaykum \n"+message.from_user.first_name+
                     "\n@"+message.from_user.username)

if __name__ == '__main__':
    bot.polling(none_stop=True)
