from aiogram import types, Dispatcher
from create_bot import bot
from aiogram.dispatcher.filters import Text
from keyboards import *
from aiogram.types import ReplyKeyboardRemove


async def start(message: types.Message):
    #if message.from_user.id == 544150026:
    await bot.send_message(message.from_user.id, 'Дароу, кэп', reply_markup=kb_admin_start())
    #else:
    await bot.send_message(message.from_user.id, 'Дароу', reply_markup=kb_client_start())


async def buy(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите товар', reply_markup=kbi_client_product())




def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(buy, Text(equals='Выбрать товар', ignore_case=True))