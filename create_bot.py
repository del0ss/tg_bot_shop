from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage

bot = Bot(token="1502879233:AAFvUgmpM9ME3pm_GdXRgFp1l4uK4GofCqA")
dp = Dispatcher(bot)