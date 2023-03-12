

"""**********************************КЛИЕНТСКАЯ ЧАСТЬ**********************************"""


from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


async def commands_start(msg : types.Message):
    try:
        await bot.send_message(msg.from_user.id, f"Приятного аппетита!", reply_markup=kb_client)
        await msg.delete()
    except:
        await msg.reply('Общение с ботом через лс, напишите ему: \nhttps://t.me/AssistanBot_ChatBot')

async def pizza_open_command(msg : types.Message):
    await bot.send_message(msg.from_user.id, "Вс-Чт с 9:00 до 20:00\nПт-Сб с 10:00 до 23:00")

async def pizza_place_command(msg : types.Message):
    await bot.send_message(msg.from_user.id, "ул. Колбасная 15")

async def pizza_menu_command(msg : types.Message):
    await sqlite_db.sql_read(msg)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])