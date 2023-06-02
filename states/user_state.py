from aiogram.dispatcher import FSMContext
from loader import storage, bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types, Dispatcher
from database.user_info import create_profile, edit_profile
from keyboards.reply_kb import teacher_list_kb, ok_kb, lang_lev_kb
from aiogram.types import ReplyKeyboardRemove
from database.user_info import db_start
from datetime import datetime


class StudentRegister(StatesGroup):
    name = State()
    age = State()
    level = State()
    period = State()
    number_phone = State()
    ok = State()


async def load_name(message: types.Message, state: FSMContext):
    if len(message.text) < 10:
        await message.answer("Iltimos, ma'lumotlaringizni to'g'ri kiriting")
    else:
        async with state.proxy() as data:
            data['name'] = message.text
        await message.reply('Sizning yoshingiz', reply_markup=ReplyKeyboardRemove())
        await StudentRegister.next()


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Yoshingizni raqamda ko'rsating")
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await message.reply("Ingliz tilidagi darajangizni tanlang", reply_markup=lang_lev_kb())
        await StudentRegister.next()


async def load_level(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['level'] = message.text
        data['teacher'] = datetime.now().replace(microsecond=0)

    user_id = str(message.from_user.id)
    db, cur = await db_start()

    if db and cur:
        await edit_profile(state, user_id, data['course'], cur)
        await message.reply("O'zingizga qulay bo'lgan vaqtni yozing.\n(00:00) formatida"
                            "\ndarslar 2 soat davom etadi! ", reply_markup=ReplyKeyboardRemove())
        await StudentRegister.next()
    else:
        await message.reply('An error occurred while initializing the database. Please try again later.')


async def load_time_ed(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['period'] = message.text
    await message.reply('Telefon raqamingizni kiriting: 998xxxxxxxxx')
    await StudentRegister.next()


async def load_phone(message: types.Message, state: FSMContext):
    if not message.text.isdigit() or len(message.text) != 12:
        await message.answer("Telefon raqamingizni yuqorida ko'rsatilgan formatda kiriting!")
    else:
        async with state.proxy() as data:
            data['number_phone'] = message.text
        await message.answer("Bizning botimizdan ro'yxatdan o'tganingizdan mamnunmiz", reply_markup=ok_kb())
        await StudentRegister.next()


async def load_ok(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ok'] = message.text

    user_id = str(message.from_user.id)
    db, cur = await db_start()

    await create_profile(user_id, data['course'], cur)
    await edit_profile(state, user_id, data['course'], cur)
    await message.reply("Ma'lumotlaringiz muvofaqqiyatli saqlandi👌\n"
                        "Siz bilan 24 soat ichida bog'lanamiz☺️", reply_markup=ReplyKeyboardRemove())

    # Send notification to admin
    admin_user_id = 5489832625  # Replace with the actual admin user ID
    admin_message = f"New user registered!\nUser ID: {user_id}"
    await bot.send_message(admin_user_id, admin_message)

    await state.finish()


def register_handler_regis_student(dp: Dispatcher):
    dp.register_message_handler(load_name, state=StudentRegister.name)
    dp.register_message_handler(load_age, state=StudentRegister.age)
    dp.register_message_handler(load_level, state=StudentRegister.level)
    # dp.register_message_handler(load_teacher, state=StudentRegister.teacher)
    dp.register_message_handler(load_time_ed, state=StudentRegister.period)
    dp.register_message_handler(load_phone, state=StudentRegister.number_phone)
    dp.register_message_handler(load_ok, state=StudentRegister.ok)

