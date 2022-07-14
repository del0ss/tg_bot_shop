import os
import re
from datetime import datetime
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove

from keyboards import TgKeyboards, TgInlineKeyboards
from states import Report


class TgHandlers:
    def __init__(self, repository, bot):
        self.repository = repository
        self.bot = bot

    # -------------------------START--------------------------
    async def start(self, msg: types.Message):
        await self.bot.send_message(
            msg.from_user.id,
            'Здравствуйте',
            reply_markup=TgInlineKeyboards.menu())

    async def menu(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Мейн меню', reply_markup=TgInlineKeyboards.menu())

    # -------------------------END START--------------------------

    # -------------------------MENU 1 --------------------------
    async def show(self, callback_query: types.CallbackQuery):
        answ = self.repository.getRate()
        await callback_query.message.edit_text(f'{answ}', reply_markup=TgInlineKeyboards.thirdMenu())

    # -------------------------END MENU 1--------------------------

    # -------------------------MENU 2 --------------------------
    async def bonus(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Бонус', reply_markup=TgInlineKeyboards.secondMenu())

    async def callCenter(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Колл цент', reply_markup=TgInlineKeyboards.secondMenu2())

    async def offlineSell(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Оффлайн продажи', reply_markup=TgInlineKeyboards.secondMenu2())

    async def storage(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Хранилище', reply_markup=TgInlineKeyboards.secondMenu2())

    async def delivery(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Доставка', reply_markup=TgInlineKeyboards.secondMenu2())

    async def lates(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Слабые', reply_markup=TgInlineKeyboards.secondMenu3Low())

    async def up(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Какоц процент?', reply_markup=TgInlineKeyboards.secondMenu3())

    async def proc1(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Слабые', reply_markup=TgInlineKeyboards.secondMenu3Low())

    async def proc2(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Умеренные', reply_markup=TgInlineKeyboards.secondMenu3Medium())

    async def proc3(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Сильные', reply_markup=TgInlineKeyboards.secondMenu3Power())

    async def upUnprem(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Повышение з/п без учета премии', reply_markup=TgInlineKeyboards.menu())

    async def graph(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Гибкий график', reply_markup=TgInlineKeyboards.menu())

    async def eat(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Компенсация питания', reply_markup=TgInlineKeyboards.menu())

    async def car(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Предоставление автомобиля для снужебных целей курьерам',
                                               reply_markup=TgInlineKeyboards.menu())

    async def chill(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Путёвки на отдых', reply_markup=TgInlineKeyboards.menu())

    async def medic(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Медицинское страхование', reply_markup=TgInlineKeyboards.menu())

    async def fullPrice(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Полная оплата больничного листа', reply_markup=TgInlineKeyboards.menu())

    async def bonus_chill(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Дополнительный выходной день', reply_markup=TgInlineKeyboards.menu())

    async def help_work(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Помощь в дальнейшем трудоустройстве',
                                               reply_markup=TgInlineKeyboards.menu())

    async def subtop(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Subtopic 5', reply_markup=TgInlineKeyboards.menu())

    async def ticket_event(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Деньги, билеты на мероприятия', reply_markup=TgInlineKeyboards.menu())

    async def add_parking(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Предоставление парковочного места',
                                               reply_markup=TgInlineKeyboards.menu())

    async def discount(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Скидка на продукты компании и компаний партнёров',
                                               reply_markup=TgInlineKeyboards.menu())

    async def child_posobie(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Дополнительное пособие по уходу за ребёнком',
                                               reply_markup=TgInlineKeyboards.menu())

    async def chill_child(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Дополнительные дни к отпуску по уходу за ребёнком',
                                               reply_markup=TgInlineKeyboards.menu())

    async def format_work(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Удалённый формат работы по желаию сотрудника',
                                               reply_markup=TgInlineKeyboards.menu())

    # -------------------------END MENU 2--------------------------

    # -------------------------MENU 3 --------------------------
    async def news(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Фому хотят уволить, потому что он не разумно потратил деньги.',
                                               reply_markup=TgInlineKeyboards.thirdMenu())

    # -------------------------END MENU 3--------------------------

    # -------------------------MENU 4 --------------------------
    async def implement(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Осущетвить что?', reply_markup=TgInlineKeyboards.fourthMenu())

    async def prod(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Заказ товаров со склада', reply_markup=TgInlineKeyboards.menu())

    async def list(self, callback_query: types.CallbackQuery):
        answ = self.repository.getSneakers()
        await callback_query.message.edit_text(f'{answ}', reply_markup=TgInlineKeyboards.thirdMenu())

    # -------------------------END MENU 4--------------------------

    # -------------------------MENU 5 --------------------------
    async def report(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Отправить анонимно или от вашего имени?',
                                               reply_markup=TgInlineKeyboards.reportMenu())
        await Report.first()

    async def anon(self, callback_query: types.CallbackQuery):
        await callback_query.message.edit_text('Опишите ситуацию', reply_markup=TgInlineKeyboards.cancel())
        await Report.title_problem.set()

    async def name(self, callback_query: types.CallbackQuery):
        await Report.next()
        await callback_query.message.edit_text(f'Напишите ваше имя', reply_markup=TgInlineKeyboards.cancel())

    async def discriptionProblem(self, msg: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['name'] = msg.text
        await Report.next()
        await self.bot.send_message(msg.from_user.id, 'Опишите ситуацию', reply_markup=TgInlineKeyboards.cancel())

    async def titleProblem(self, msg: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['discription'] = msg.text
        await Report.next()
        await self.bot.send_message(msg.from_user.id, 'Назовите проблему', reply_markup=TgInlineKeyboards.cancel())

    async def solutionProblem(self, msg: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['title'] = msg.text
        await Report.next()
        await self.bot.send_message(msg.from_user.id, ' Какие пути решения Вы видите?',
                                    reply_markup=TgInlineKeyboards.cancel())

    async def agrumentsProblem(self, msg: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['solution'] = msg.text
        await Report.next()
        await self.bot.send_message(msg.from_user.id, 'Приведите аргументы в пользу своей позиции',
                                    reply_markup=TgInlineKeyboards.cancel())

    async def end(self, msg: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['args'] = msg.text
        await state.finish()
        await self.bot.send_message(msg.from_user.id,
                                    'Благодарим за предоставленную информацию! Ваша заявка будет рассмотренная в ближайшее время.',
                                    reply_markup=TgInlineKeyboards.menu())
        await self.bot.send_message(-682476648, ', \n'.join(data.values()))

    async def cancel_registration(self, callback_query: types.CallbackQuery, state: FSMContext):
        if await state.get_state() is None:
            return
        await state.finish()
        await callback_query.message.edit_text('Вы отменили обращение', reply_markup=TgInlineKeyboards.menu())

    # -------------------------END MENU 5--------------------------
