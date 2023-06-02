from aiogram import types, Dispatcher
from database.user_info import get_profiles, db_start
from loader import dp


# 5489832625


async def show_profiles(message: types.Message):
    db, cur = await db_start()
    profiles = await get_profiles(cur)

    if profiles:
        text = ""
        for profile in profiles:
            user_id, name, age, level, teacher, period, number_phone, ok, course = profile

            text += f"\nName: {name}\nAge: {age}\nLevel: {level}" \
                    f"\nConvenient time: {period}\n" \
                    f"Number: {number_phone}\nCourse: {course}\n\nDate register: : {teacher}\n{user_id}"

        if message.from_user.id == 5489832625:
            await message.reply(text)
        else:
            await message.answer('У вас нет прав доступа')
    else:
        await message.reply("No profiles found.")


def register_handler_database(dp: Dispatcher):
    dp.register_message_handler(show_profiles, commands=['britify1997'])