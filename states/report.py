from aiogram.dispatcher.filters.state import State, StatesGroup


class Report(StatesGroup):
    name = State()
    discription_problem = State()
    title_problem = State()
    solution_problem = State()
    agruments_problem = State()
    end = State()