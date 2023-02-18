from config import dp
from aiogram import types
from wolf import qu
from random import randint as RI

from config import bot

users = {}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global users

    # await message.answer(f'Привет, {message.from_user.first_name}, лови мудрость!')
    # li = qu.get()
    # num = RI(0, len(li)-1)
    # await message.answer(li[num])
    # print(message.from_user.id, message.from_user.username)
    # await bot.send_message('5076430555', message)

    users[message.from_user.id] = 0
    await message.answer(f'Все ок')


@dp.message_handler(commands=['quote'])
async def game(message: types.Message):
    global users

    if message.from_user.id in users:
        users[message.from_user.id] = 1
        await message.answer(f'Отправь сообщение в чат и получишь мудрость!')
    else:
        await message.answer(f'Сначала /start')

@dp.message_handler(commands=['echo'])
async def game(message: types.Message):
    global users

    if message.from_user.id in users:
        users[message.from_user.id] = 2
        await message.answer(f'Эхо функция запущена, напиши ченить')
    else:
        await message.answer(f'Сначала /start')

@dp.message_handler()
async def start(message: types.Message):
    global users

    if message.from_user.id in users:

        if users[message.from_user.id] == 0:
            await message.answer(f'Выбери команду:\n/quote \n/echo')
            
        elif users[message.from_user.id] == 1:
            li = qu.get()
            num = RI(0, len(li)-1)
            await message.answer(li[num])
            print(message.from_user.id, message.from_user.username)
            await bot.send_message('5076430555', message)

        elif users[message.from_user.id] == 2:
            await message.answer(message.text)
    else:
        await message.answer(f'Жми /start')