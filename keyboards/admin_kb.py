from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

def kb_admin_start():
    kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
    bttn = ['Выбрать товар', 'Корзина', 'Админ панель']
    return kb_admin.add(*bttn)

def kb_admin_panel():
    kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
    bttn = ['Добавить новый товар', 'Редактировать товар', ]
    return kb_admin.add(*bttn)

