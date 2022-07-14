from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class TgInlineKeyboards:
    @staticmethod
    def _kbi_wrapper(func):
        def wrapped():
            keyboard = InlineKeyboardMarkup(row_width=2)
            return keyboard.add(*func())

        return wrapped

    @_kbi_wrapper
    @staticmethod
    def menu():
        return [InlineKeyboardButton(text='Посмотреть текущий рейтинг', callback_data='show'),
                InlineKeyboardButton(text='Бонусная система', callback_data='bonus'),
                InlineKeyboardButton(text='Новости компании', callback_data='news'),
                InlineKeyboardButton(text='Осуществить', callback_data='implement'),
                InlineKeyboardButton(text='Написать проблему', callback_data='report')]

    @_kbi_wrapper
    @staticmethod
    def firstMenu():
        return [InlineKeyboardButton(text='Обсудить с Котовой', callback_data='kotova'),
                InlineKeyboardButton(text='Берём готовые данные из дока', callback_data='rand'),
                InlineKeyboardButton(text='Основное меню', callback_data='menu')
                ]

    @_kbi_wrapper
    @staticmethod
    def secondMenu():
        return [InlineKeyboardButton(text='Call-центр', callback_data='call_center'),
                InlineKeyboardButton(text='Отдел оффлайн-продаж', callback_data='offline_sell'),
                InlineKeyboardButton(text='Складной отдел', callback_data='storage'),
                InlineKeyboardButton(text='Отдел доставки', callback_data='delivery'),
                InlineKeyboardButton(text='Основное меню', callback_data='menu')
                ]

    @_kbi_wrapper
    @staticmethod
    def secondMenu2():
        return [InlineKeyboardButton(text='Не буду опаздывать', callback_data='lates'),
                InlineKeyboardButton(text='Превышу планку продаж на', callback_data='up'),
                InlineKeyboardButton(text='Основное меню', callback_data='menu')
                ]

    @_kbi_wrapper
    @staticmethod
    def secondMenu3():
        return [InlineKeyboardButton(text='7%', callback_data='proc1'),
                InlineKeyboardButton(text='15%', callback_data='proc2'),
                InlineKeyboardButton(text='25%', callback_data='proc3'),
                InlineKeyboardButton(text='Основное меню', callback_data='menu')
                ]


    @_kbi_wrapper
    @staticmethod
    def thirdMenu():
        return [InlineKeyboardButton(text='Основное меню', callback_data='menu')]

    @_kbi_wrapper
    @staticmethod
    def cancel():
        return [InlineKeyboardButton(text='Отмена', callback_data='cancel')]

    @_kbi_wrapper
    @staticmethod
    def fourthMenu():
        return [InlineKeyboardButton(text='Заказ товаров со склада', callback_data='prod'),
                InlineKeyboardButton(text='Список товаров на складе', callback_data='list'),
                InlineKeyboardButton(text='Основное меню', callback_data='menu')]

    @_kbi_wrapper
    @staticmethod
    def reportMenu():
        return [InlineKeyboardButton(text='Анонимно', callback_data='anon'),
                InlineKeyboardButton(text='Написать имя', callback_data='name'),
                InlineKeyboardButton(text='Отмена', callback_data='cancel')]

    @_kbi_wrapper
    @staticmethod
    def secondMenu3Power():
        return [InlineKeyboardButton(text='Повышение з/п без учета премии', callback_data='up_unprem'),
                InlineKeyboardButton(text='Гибкий график', callback_data='graph'),
                InlineKeyboardButton(text='Компенсация питания', callback_data='eat'),
                InlineKeyboardButton(text='Предоставление автомобиля для снужебных целей курьерам', callback_data='car'),
                InlineKeyboardButton(text='Путёвки на отдых', callback_data='chill'),
                InlineKeyboardButton(text='Основное меню', callback_data='menu')
                ]

    @_kbi_wrapper
    @staticmethod
    def secondMenu3Medium():
        return [InlineKeyboardButton(text='Медицинское страхование', callback_data='medic'),
                InlineKeyboardButton(text='Полная оплата больничного листа', callback_data='full_price'),
                InlineKeyboardButton(text='Дополнительный выходной день', callback_data='bonus_chill'),
                InlineKeyboardButton(text='Помощь в дальнейшем трудоустройстве', callback_data='help_work'),
                InlineKeyboardButton(text='Subtopic 5', callback_data='subtop'),
                InlineKeyboardButton(text='Основное меню', callback_data='menu')
                ]

    @_kbi_wrapper
    @staticmethod
    def secondMenu3Low():
        return [InlineKeyboardButton(text='Деньги, билеты на мероприятия', callback_data='ticket_event'),
                InlineKeyboardButton(text='Предоставление парковочного места', callback_data='add_parking'),
                InlineKeyboardButton(text='Скидка на продукты компании и компаний партнёров', callback_data='discount'),
                InlineKeyboardButton(text='Дополнительное пособие по уходу за ребёнком', callback_data='child_posobie'),
                InlineKeyboardButton(text='Дополнительные дни к отпуску по уходу за ребёнком', callback_data='chill_child'),
                InlineKeyboardButton(text='Удалённый формат работы по желаию сотрудника', callback_data='format_work'),
                InlineKeyboardButton(text='Основное меню', callback_data='menu')
                ]