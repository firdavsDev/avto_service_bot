from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from loader import dp
from geopy.distance import geodesic
from states.loaction_state import LocationState
from aiogram.dispatcher import FSMContext

from utils.db_api.db import Database
from keyboards.inline.service_type_btn import categoryMenu


db = Database(path_to_db="data.db")
# Avto servislar ma'lumotlari
avto_servislar = {
    "Avto elektrik": db.get_data("Avto_elektrik", ["location", "phone_number"]),
    "Moy almashtirish": db.get_data("Moy_almashtirish", ["location", "phone_number"]),
    "Avto yurish qismini ta'mirlash": db.get_data("Avto_yurish_qismini_tamirlash", ["location", "phone_number"]),
    "Kuzovchi": db.get_data("Kuzovchi", ["location", "phone_number"]),
    "Avto diagnostika": db.get_data("Avto_diagnostika", ["location", "phone_number"]),
    "Avto detailing": db.get_data("Avto_detailing", ["location", "phone_number"])
}


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum , {message.from_user.full_name} Avto servis turini tanlang:", reply_markup=categoryMenu)
    await LocationState.Choice_service.set()


@dp.callback_query_handler(lambda text: [text == i for i in ['Avto elektrik', 'Moy almashtirish', "Avto yurish qismini ta'mirlash", 'Kuzovchi', 'Avto diagnostika', 'Avto detailing']],  state=LocationState.Choice_service)
async def buy_courses(call: CallbackQuery, state: FSMContext):
    callback_data = call.data
    print("avto_servislar", avto_servislar)
    selected_service = avto_servislar[callback_data]
    await state.update_data(
        {"selected_service": selected_service}
    )
    await call.message.delete()
    await call.message.answer("Hozirgi joylashuvingizni yuboring:")
    await LocationState.Location.set()


@dp.message_handler(content_types=types.ContentTypes.LOCATION, state=LocationState.Location)
async def process_location_step(message: types.Message, state: FSMContext):
    user_location = (message.location.latitude, message.location.longitude)
    data = await state.get_data()
    selected_service = data.get('selected_service')
    nearest_services = find_nearest_services(user_location, selected_service)

    for i, (service_info, distance) in enumerate(nearest_services, start=1):
        print("service_info", service_info)
        print("distance", distance)
        print("i", i)
        service_info_full = f"{i}.Masofa: {distance:.2f} km\n"
        service_info_full += f"Telefon raqami: {service_info['phone_number']}"

        await message.answer(service_info_full)
        await message.answer_location(latitude=service_info['location'][0], longitude=service_info['location'][1])
    await state.finish()


def find_nearest_services(user_location, services, count=3):
    nearest_services = []
    print("services", services)
    # convert 'location': '(41.345678, 69.345678)', to tuple in every service
    for service in services:
        service['location'] = tuple(map(float,
                                        service['location'].strip('()').split(', ')))

    sorted_services = sorted(services, key=lambda x: geodesic(
        user_location, x['location']).kilometers)
    for i in range(min(count, len(sorted_services))):
        service_info = sorted_services[i]
        distance = geodesic(user_location, service_info['location']).kilometers
        nearest_services.append((service_info, distance))
    return nearest_services
