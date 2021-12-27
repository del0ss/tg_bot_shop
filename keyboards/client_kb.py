from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

def kb_client_start():
    kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
    bttn = ['Выбрать товар', 'Корзина']
    return kb_client.add(*bttn)

def kbi_client_product():
    kb_client = InlineKeyboardMarkup(row_width=1)
    bttn = [InlineKeyboardButton('Следущий товар'), InlineKeyboardButton('Предыдущий товар'), InlineKeyboardButton('Корзина')]
    return kb_client.add(*bttn)

