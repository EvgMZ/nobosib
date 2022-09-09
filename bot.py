
#pip install aiogram

from aiogram import Bot, Dispatcher, executor, types

token = '5684557515:AAGKAHKtToijdgM1S_X5tTE48pGeXHSQu2g'


bot =  Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler()
def start_procces(msg: types.Message):
    return msg.reply(msg.text[::-1])


executor.start_polling(dp)
