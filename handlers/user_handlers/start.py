from aiogram import Dispatcher, types
from keyboards.reply_kb import list_of_course_teach_kb


async def cmd_start(message: types.Message):
    await message.answer("“<b>Britify</b> - Specialized in IELTS” ning ro’yxatdan o’tish botiga xush kelibsiz!\n\n"
                         "<b>Britify</b> - <em>FAQAT IELTS 9.0</em>\n\n"
                        "Nima uchun aynan bizni tanlashingiz kerak?\n\n"
                        "✔️Tajribali ustozlar (7-8) ️\n"
                        "✔️Buyuk Britaniya ta’lim tizimi (Oxford University Press, Cambridge University Press)️\n"
                        "✔️Bepul co-working hudud\n"
                        "✔️Bepul Speaking treninglar\n",
                        reply_markup=list_of_course_teach_kb(), parse_mode='html')

    await message.delete()


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])