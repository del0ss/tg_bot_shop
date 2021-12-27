from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import bot
from keyboards import *
from data_base import sqlite_db
admins = [544150026, 1200047091]



async def admin_panel(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ваша админ панель', reply_markup=kb_admin_panel())


async def produsts_set(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите товар для редактирования: ')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(admin_panel, Text(equals='Админ панель', ignore_case=True), chat_id=[544150026, 1200047091])
    dp.register_message_handler(admin_panel, Text(equals='Редактировать товар', ignore_case=True), chat_id=[544150026, 1200047091])











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