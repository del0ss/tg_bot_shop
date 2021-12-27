from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from create_bot import bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from data_base import sqlite_db
admins = [544150026, 1200047091]

class AddNewProduct(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def start_prod(message: types.Message):
    await AddNewProduct.photo.set()
    await message.reply('Загрузите картинку')


#1
async def photo_prod(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await AddNewProduct.next()
    await message.reply('Введите название товара')


#2
async def name_prod(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await AddNewProduct.next()
    await message.reply('Введите описание товара')


#3
async def descr_prod(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await AddNewProduct.next()
    await message.reply('Введите цену товара')


#4
async def price_prod(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text + ' rub'
    await sqlite_db.sql_add_menu(state)
    await state.finish()
    await bot.send_message(message.from_user.id, 'Товар добавлен!')


async def cancel(message: types.Message, state=FSMContext):
    if await state.get_state() is None: return
    await state.finish()
    await message.reply('Отмена')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state="*", chat_id=admins)
    dp.register_message_handler(start_prod, Text(equals='Добавить новый товар', ignore_case=True), state=None, chat_id=admins)
    dp.register_message_handler(photo_prod, content_types=['photo'], state=AddNewProduct.photo, chat_id=admins)
    dp.register_message_handler(name_prod, state=AddNewProduct.name, chat_id=admins)
    dp.register_message_handler(descr_prod, state=AddNewProduct.description, chat_id=admins)
    dp.register_message_handler(price_prod, state=AddNewProduct.price, chat_id=admins)