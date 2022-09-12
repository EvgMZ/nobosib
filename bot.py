
#pip install aiogram

from aiogram import Bot, Dispatcher, executor, types
import os
token_telegram = '5684557515:AAGKAHKtToijdgM1S_X5tTE48pGeXHSQu2g'


bot = Bot(token=token_telegram)

dp = Dispatcher(bot)


@dp.message_handler(commands=['photos'])
async def send_phs(msg: types.Message):
    if os.getcwd() != '/home/kkbs/s/nobosib/cats':
        os.chdir(os.getcwd() + '/cats')
    files = os.listdir(os.getcwd())
    for file in files:
        f = open(file, 'rb')
        f = f.read()
        await bot.send_photo(msg.chat.id, f)


@dp.message_handler(commands=['tw'])
async def send_tw(msg: types.Message):
    await bot.send_message(msg.chat.id, 'hello')
    await bot.send_message(msg.chat.id, 'hel12lo')


@dp.message_handler(commands=['photo'])
def send_ph(msg: types.Message):
    file = open('cats/photo1.png', 'rb')
    file = file.read()
    return bot.send_photo(msg.chat.id, file)


@dp.message_handler(commands=['start'])
def start(msg: types.Message):
    f = open('monday.txt', 'rb')
    f = f.read()
    return bot.send_message(msg.from_user.id, f)


@dp.message_handler()
def start_procces(msg: types.Message):
    return msg.reply(msg.text[::-1])




executor.start_polling(dp)
