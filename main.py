from aiogram.utils import executor
from loader import dp
from handlers.user_handlers import start, list_of_courses_and_teach
from states import user_state
from database.user_info import db_start
from handlers.admin_handlers import admin


async def on_startup(_):
    await db_start()
    print('Бот вышел в онлайн')


start.register_handler_start(dp)
list_of_courses_and_teach.register_handler_list_cour(dp)
user_state.register_handler_regis_student(dp)
admin.register_handler_database(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)