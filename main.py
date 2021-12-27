from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, addproduct
from data_base import sqlite_db

async def online(_):
    print('Bot started')
    sqlite_db.sqlStart()

client.register_handlers_client(dp)
admin.register_handlers_client(dp)
addproduct.register_handlers_client(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=online)
