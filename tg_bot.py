from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='5779711337:AAHd01KUTa6xl8YPeQGH1_iUUL3ZwwHsBq0')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Hello, Anna!')






if __name__ == '__main__':
    executor.start_polling(dp)
