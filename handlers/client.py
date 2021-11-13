from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Дароу', reply_markup=kb_client)

async def buy(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите товар', reply_markup=ReplyKeyboardRemove())

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(buy, Text(equals='Купить'))