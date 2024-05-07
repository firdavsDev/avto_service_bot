from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Avto elektrik", callback_data="Avto elektrik"),
        InlineKeyboardButton(text="Moy almashtirish", callback_data="Moy almashtirish"),
    ],
    [
        InlineKeyboardButton(text="Avto yurish qismini ta'mirlash", callback_data="Avto yurish qismini ta'mirlash"),
        InlineKeyboardButton(text="Kuzovchi", callback_data="Kuzovchi"),
    ],
    [
        InlineKeyboardButton(text="Avto diagnostika", callback_data="Avto diagnostika"),
        InlineKeyboardButton(text="Avto detailing", callback_data="Avto detailing"),
    ],
    
])
