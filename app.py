from aiogram import executor

from loader import dp
import middlewares
import filters
import handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api.db import Database


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)

    # DB ni yaratish
    db = Database(path_to_db="data.db")
    db.create_table("services", ["service_name", "location", "phone_number"])
    db.close()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
