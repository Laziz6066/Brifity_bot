from aiogram.dispatcher import FSMContext
from loader import storage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types, Dispatcher
from database.user_info import create_profile, edit_profile
from keyboards.reply_kb import teacher_list_kb, ok_kb
from aiogram.types import ReplyKeyboardRemove


class StudentRegister(StatesGroup):
    name = State()
    age = State()
    level = State()
    teacher = State()
    period = State()
    number_phone = State()
    ok = State()


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.reply('Сколько тебе лет?', reply_markup=ReplyKeyboardRemove())
    await StudentRegister.next()


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await message.reply('Напишите свой уровень владения английским языком')
    await StudentRegister.next()


async def load_level(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['level'] = message.text
    await message.reply('Выберите учителя', reply_markup=teacher_list_kb())
    await StudentRegister.next()


async def load_teacher(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['teacher'] = message.text
    await message.reply('Напишите удобное для вас время', reply_markup=ReplyKeyboardRemove())
    await StudentRegister.next()


async def load_time_ed(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['period'] = message.text
    await message.reply('Введите номер телефона')
    await StudentRegister.next()


async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number_phone'] = message.text
    await message.answer('Для подтверждения ваших данных нажмите ок', reply_markup=ok_kb())
    await StudentRegister.next()


async def load_ok(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ok'] = message.text

    user_id = str(message.from_user.id)
    await create_profile(user_id)
    await edit_profile(state, user_id)

    await message.reply('Ваша анкета успешно создана', reply_markup=ReplyKeyboardRemove())
    await state.finish()


def register_handler_regis_student(dp: Dispatcher):
    dp.register_message_handler(load_name, state=StudentRegister.name)
    dp.register_message_handler(load_age, state=StudentRegister.age)
    dp.register_message_handler(load_level, state=StudentRegister.level)
    dp.register_message_handler(load_teacher, state=StudentRegister.teacher)
    dp.register_message_handler(load_time_ed, state=StudentRegister.period)
    dp.register_message_handler(load_phone, state=StudentRegister.number_phone)
    dp.register_message_handler(load_ok, state=StudentRegister.ok)

