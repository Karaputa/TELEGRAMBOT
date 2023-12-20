import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import dispatcher
from aiogram import executor
import random
import string

API_TOKEN = '6919449758:AAHR0O5dNPvQdsMRQ2-HRbcldhtCBIMO5uQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Добро пожаловать! Я бот-генератор паролей. Пожалуйста, введите длину пароля, которая вам нужна.")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Доступные команды: \n/start - запустить бота \n/help - список команд")

@dp.message_handler()
async def generate_password(message: types.Message):
    try:
        length = int(message.text)
        password = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton('Хорошо'), types.KeyboardButton('Еще вариант'))
        await message.reply(f"Your password: {password}", reply_markup=keyboard)
    except ValueError:
        await message.reply("Пожалуйста, введите цифру.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)