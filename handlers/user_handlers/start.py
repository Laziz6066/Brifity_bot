from aiogram import Dispatcher, types
from keyboards.reply_kb import list_of_course_teach_kb


async def cmd_start(message: types.Message):
    await message.reply(f'Hello {message.from_user.full_name}!\n'
                        f'I am a bot of the Britify training center\n',
                        reply_markup=list_of_course_teach_kb())


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])