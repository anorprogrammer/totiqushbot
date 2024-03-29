import logging

from aiogram import Bot, Dispatcher, executor, types

from config import API_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
