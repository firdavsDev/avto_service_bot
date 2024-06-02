from aiogram import types

from loader import dp
from utils.db_api.db import Database

db = Database(path_to_db="data.db")

avto_servislar = db.get_data(
    "Avto_elektrik", ["location", "phone_number", "service_name"]),


@dp.message_handler(commands=['service'])
async def bot_services(message: types.Message):
    # get Avto elektrik services
    text = []
    # avto_servislar is list of tuples with one element in it
    for servis in avto_servislar:
        # servis is a tuple with one element in it

        for servis_info in servis:
            # add phone number and service name to the text
            text.append(
                f"🔧 {servis_info['service_name']} \n📞 {servis_info['phone_number']}")
    # send all services to the user
    await message.answer("\n\n".join(text))
