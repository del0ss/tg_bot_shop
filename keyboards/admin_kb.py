from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
bttn = ['Купить', 'Корзина', 'Админ панель']
kb_admin.add(*bttn)