from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
bttn = ['Купить', 'Корзина']
kb_client.add(*bttn)
