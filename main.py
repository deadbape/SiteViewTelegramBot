import aiogram
import requests
from aiogram import Bot, Dispatcher, types, executor

from data import config as config 


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print(message.text, message.from_user.id)
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.chat.id, 'I get help you with view sites anonymously! <Send me link>')


@dp.message_handler()
async def make_screen(message: types.Message):
    print(message.text, message.from_user.id) #log terminal
    user_link = str(message.text)
    r_ul = requests.get(f"https://webshot.deam.io/{user_link}/?width=1440&height=1024?type=png")
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_photo(
        message.chat.id,
        photo=r_ul.content,
        caption=f'web == {user_link}')
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,)
