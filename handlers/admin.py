from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from create_bot import bot
from aiogram.dispatcher.filters.state import State, StatesGroup
admins = [544150026, 1200047091]

class AddNewProduct(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

async  def admin(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы прошли провеку на админа', reply_markup='')


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
        data['description'] = message.text + ' rub'
    await state.finish()


async def cancel(message: types.Message, state=FSMContext):
    if await state.get_state() is None: return
    await state.finish()
    await message.reply('Отмена')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state="*", chat_id=admins)
    dp.register_message_handler(start_prod, Text(equals='Загрузить', ignore_case=True), state=None, chat_id=admins)
    dp.register_message_handler(photo_prod, content_types=['photo'], state=AddNewProduct.photo, chat_id=admins)
    dp.register_message_handler(name_prod, state=AddNewProduct.name, chat_id=admins)
    dp.register_message_handler(descr_prod, state=AddNewProduct.description, chat_id=admins)
    dp.register_message_handler(price_prod, state=AddNewProduct.price, chat_id=admins)


# from aiogram.dispatcher.filters import BoundFilter
#
# class MyFilter(BoundFilter):
#     key = 'is_admin'
#
#     def __init__(self, is_admin):
#         self.is_admin = is_admin
#
#     async def check(self, message: types.Message):
#         member = await bot.get_chat_member(message.chat.id, message.from_user.id)
#         return member.is_chat_admin()
#
# dp.filters_factory.bind(MyFilter)
#
# @dp.message_handler(is_admin=True)
# async def ...    ЭТО ДЛЯ ПРОВЕРКИ АДМИНА В БЕСЕДЕ