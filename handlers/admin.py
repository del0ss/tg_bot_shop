from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot


class AddNewProduct(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

@dp.message_handler(commands='dada', state=None)
async def addProductStart(message: types.Message):
    await AddNewProduct.photo.set()
    await message.reply('Загрузите картинку')

#1
@dp.message_handler(content_types=['photo'], state=AddNewProduct.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await AddNewProduct.next()
    await message.reply('Введите название товара')

#2
@dp.message_handler(state=AddNewProduct.name)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await AddNewProduct.next()
    await message.reply('Введите описание товара')

#3
@dp.message_handler(state=AddNewProduct.description)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await AddNewProduct.next()
    await message.reply('Введите цену товара')

#4
@dp.message_handler(state=AddNewProduct.description)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = float(message.text)
    await state.finish() # СДЕЛАТЬ АДМИН ПАНЕЛЬ ДЛЯ ЗАГРУЗКИ ТОВАРА