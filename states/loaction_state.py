from aiogram.dispatcher.filters.state import StatesGroup, State


class LocationState(StatesGroup):
    Choice_service = State()
    Location = State()
