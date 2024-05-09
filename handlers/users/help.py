from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp

excavator_db = [
    {
        "name": "Evakuator xizmati",
        "phone": "+998882333332"
    },
    {
        "name": "EVAKUATOR.UZ",
        "phone": "+998946666663"
    },
    {
        "name": "Evakuator 1331",
        "phone": "+998993150166"
    },
    {
        "name": "Эвакуатор",
        "phone": "+998901106666"
    },
    {
        "name": "Эвакуатор в Ташкенте",
        "phone": "+998983010009"
    },
    {
        "name": "Эвакуатор Газалкент",
        "phone": "+998991108200"
    },

]


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):

    # loop excavator_db and get name and phone
    text = []
    for excavator in excavator_db:
        text.append(f"<b>* {excavator['name']} - {excavator['phone']} *</b>")

    await message.answer("\n".join(text))
