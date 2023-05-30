from aiogram import types, Dispatcher
from database.user_info import get_profiles
from loader import dp


async def show_profiles(message: types.Message):
    profiles = await get_profiles()
    if profiles:
        text = ""
        for profile in profiles:
            user_id, name, age, level, teacher, period, number_phone, ok = profile
            text += f"User ID: {user_id}\nName: {name}\nAge: {age}\nLevel: {level}\nTeacher: {teacher}\nPeriod: {period}\n" \
                    f"Number: {number_phone}\n\n"
        await message.reply(text)
    else:
        await message.reply("No profiles found.")



def register_handler_database(dp: Dispatcher):
    dp.register_message_handler(show_profiles, commands=['db'])